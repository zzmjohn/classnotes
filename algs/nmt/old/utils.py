# encoding=utf8

import sys, pickle, re
import cPickle, random
import numpy as np

# For special characters
reload(sys)
sys.setdefaultencoding('utf8')

_PAD = b"_PAD"
_GO = b"_GO"
_EOS = b"_EOS"
_UNK = b"_UNK"
_START_VOCAB = [_PAD, _GO, _EOS, _UNK]

PAD_ID = 0
GO_ID = 1
EOS_ID = 2
UNK_ID = 3

_WORD_SPLIT = re.compile(b"([.,!?\"':;)(])")
_DIGIT_RE = re.compile(BR"\d")

def basic_tokenizer(sentence):
    """ Split sentence into list of tokens """
    words = []
    for space_separated_item in sentence.strip().split():
        words.extend(_WORD_SPLIT.split(space_separated_item))
    return [w for w in words if w] # if w removes the ""

def get_vocab(tokenized, max_vocab_size):
    """
    Get vocab_list, vocab_dict and rev_vocab_dict given the
    tokenized sentences.
    """
    # Replace word count
    vocab = {}
    for sentence in tokenized:
        for word in sentence:
            if word in vocab:
                vocab[word] += 1
            else:
                vocab[word] = 1
    vocab_list = _START_VOCAB + sorted(vocab, key=vocab.get, reverse=True)
    if len(vocab_list) > max_vocab_size:
        vocab_list = vocab_list[:max_vocab_size]

    # Get vocab dict (word -> token) and rev dict (token -> word)
    vocab_dict = dict([(x,y) for (y,x) in enumerate(vocab_list)])
    rev_vocab_dict = {v: k for k, v in vocab_dict.iteritems()}

    return vocab_list, vocab_dict, rev_vocab_dict

def sentence_to_token_ids(sentence, vocab_dict, target_lang,
    normalize_digits=True):
    """
    Convert a single sentence of words to token ids. If it is the target
    language, we will append an EOS token to the end.
    """
    if not normalize_digits:
        # replace words not in vocab_dict with UNK_ID
        tokens = [vocab_dict.get(w, UNK_ID) for w in sentence]
    else:
        tokens = [vocab_dict.get(_DIGIT_RE.sub(b"0", w), UNK_ID)
            for w in sentence]

    # Append EOS token if target langauge sentence
    if target_lang:
        tokens.append(EOS_ID)

    return tokens


def data_to_token_ids(tokenized, vocab_dict, target_lang, normalize_digits=True):
    """
    Convert tokens into ids used vocab_dict and normalize all digits
    to 0.
    """
    data_as_tokens = []
    seq_lens = []
    max_len = max(len(sentence) for sentence in tokenized) + 1 # +1 for EOS

    for sentence in tokenized:
        token_ids = sentence_to_token_ids(sentence, vocab_dict, target_lang,
            normalize_digits)
        # Padding
        data_as_tokens.append(token_ids + [PAD_ID]*(max_len - len(token_ids)))
        # Store original sequence length
        seq_lens.append(len(token_ids))

    return np.array(data_as_tokens), np.array(seq_lens)

def process_data(datafile, max_vocab_size, target_lang):
    """
    Read the sentences from our datafiles.
    """
    tokenized = []
    fin = open(datafile)
    for line in fin.readlines():
        tokenized.append(basic_tokenizer(line))
        
    # Get vocab information
    vocab_list, vocab_dict, rev_vocab_dict = get_vocab(tokenized,
        max_vocab_size)
    
    # Convert data to token ids
    data_as_tokens, seq_lens = data_to_token_ids(tokenized, vocab_dict,
        target_lang, normalize_digits=True)

    return data_as_tokens, seq_lens, vocab_dict, rev_vocab_dict

def split_data(en_token_ids, sp_token_ids,
    en_seq_lens, sp_seq_len, train_ratio=0.8):
    """
    Split the into train and validation sets.
    """

    decoder_inputs = []
    targets = []
    # Add go token to decoder inputs and create targets
    for sentence in sp_token_ids:
        decoder_inputs.append(np.array([GO_ID] + list(sentence)))
        targets.append(np.array(([GO_ID] + list(sentence))[1:] + [0]))

    sp_token_ids = np.array(decoder_inputs)
    targets = np.array(targets)

    # Splitting index
    last_train_index = int(0.8*len(en_token_ids))

    train_encoder_inputs = en_token_ids[:last_train_index]
    train_decoder_inputs = sp_token_ids[:last_train_index]
    train_targets = targets[:last_train_index]
    train_en_seq_lens = en_seq_lens[:last_train_index]
    train_sp_seq_len = sp_seq_len[:last_train_index]

    valid_encoder_inputs = en_token_ids[last_train_index:]
    valid_decoder_inputs = sp_token_ids[last_train_index:]
    valid_targets = targets[last_train_index:]
    valid_en_seq_lens = en_seq_lens[last_train_index:]
    valid_sp_seq_len = sp_seq_len[last_train_index:]

    print "%i training samples and %i validations samples" % (
        len(train_encoder_inputs), len(valid_encoder_inputs))

    return train_encoder_inputs, train_decoder_inputs, train_targets, \
        train_en_seq_lens, train_sp_seq_len, \
        valid_encoder_inputs, valid_decoder_inputs, valid_targets, \
        valid_en_seq_lens, valid_sp_seq_len

def get_minibatch(encoder_inputs, decoder_inputs, targets, en_seq_lens, sp_seq_lens, batch_size):
    data_size = len(encoder_inputs)
    encoder_inputs_b = np.zeros((batch_size, len(encoder_inputs[0])))
    decoder_inputs_b = np.zeros((batch_size, len(decoder_inputs[0])))
    targets_b = np.zeros((batch_size, len(targets[0])))
    en_seq_lens_b = np.zeros(batch_size)
    sp_seq_lens_b = np.zeros(batch_size)
    for i in range(batch_size):
        idx = random.choice(range(data_size))    
        encoder_inputs_b[i,:] = encoder_inputs[idx]
        decoder_inputs_b[i,:] = decoder_inputs[idx]
        targets_b[i,:] = targets[idx]
        en_seq_lens_b[i] = en_seq_lens[idx]
        sp_seq_lens_b[i] = sp_seq_lens[idx]
    return encoder_inputs_b.astype(np.int64), decoder_inputs_b.astype(np.int64), targets_b.astype(np.int64), en_seq_lens_b, sp_seq_lens_b

if __name__ == "__main__": 

    print 'source vocab...'
    en_token_ids, en_seq_lens, en_vocab_dict, en_rev_vocab_dict = \
        process_data('/home/burak/Downloads/tur-eng/train.en', max_vocab_size=25000, target_lang=False)
    print 'target vocab...'
    sp_token_ids, sp_seq_lens, sp_vocab_dict, sp_rev_vocab_dict = \
        process_data('/home/burak/Downloads/tur-eng/train.tr', max_vocab_size=25000, target_lang=True)
        
    output = open('/tmp/vocab_en.pkl', 'wb')
    pickle.dump([en_token_ids, en_seq_lens, en_vocab_dict, en_rev_vocab_dict], output)
    output.close()
    output = open('/tmp/vocab_sp.pkl', 'wb')
    pickle.dump([sp_token_ids, sp_seq_lens, sp_vocab_dict, sp_rev_vocab_dict], output)
    output.close()

