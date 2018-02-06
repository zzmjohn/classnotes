

```python
import simplenet, pickle, util
net = simplenet.PolicyValue(simplenet.PolicyValue.create_network())
```

```text
Tensor("input_2:0", shape=(?, 17, 9, 9), dtype=float32)
Tensor("conv2d_4/BiasAdd:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("batch_normalization_4/batchnorm/add_1:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("conv2d_5/BiasAdd:0", shape=(?, 17, 9, 32), dtype=float32)
Tensor("batch_normalization_5/batchnorm/add_1:0", shape=(?, 17, 9, 32), dtype=float32)
------------- policy -------------------
Tensor("conv2d_6/BiasAdd:0", shape=(?, 17, 9, 2), dtype=float32)
Tensor("activation_9/Relu:0", shape=(?, 17, 9, 2), dtype=float32)
Tensor("flatten_3/Reshape:0", shape=(?, 306), dtype=float32)
policy_output Tensor("activation_10/Softmax:0", shape=(?, 82), dtype=float32)
------------- policy -------------------
Tensor("conv2d_7/BiasAdd:0", shape=(?, 17, 9, 1), dtype=float32)
Tensor("activation_11/Relu:0", shape=(?, 17, 9, 1), dtype=float32)
Tensor("flatten_4/Reshape:0", shape=(?, 153), dtype=float32)
Tensor("dense_5/BiasAdd:0", shape=(?, 256), dtype=float32)
Tensor("activation_12/Relu:0", shape=(?, 256), dtype=float32)
Tensor("dense_6/BiasAdd:0", shape=(?, 1), dtype=float32)
Tensor("dense_6/BiasAdd:0", shape=(?, 1), dtype=float32)
```

```python
import resnet, pickle, util
net = resnet.PolicyValue(resnet.PolicyValue.create_network())
```

```text
Tensor("input_1:0", shape=(?, 17, 9, 9), dtype=float32)
Tensor("conv2d/BiasAdd:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("batch_normalization/batchnorm/add_1:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("conv2d_2/BiasAdd:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("batch_normalization_2/batchnorm/add_1:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("activation_2/Relu:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("conv2d_3/BiasAdd:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("batch_normalization_3/batchnorm/add_1:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("add/add:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("activation_3/Relu:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("conv2d_4/BiasAdd:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("batch_normalization_4/batchnorm/add_1:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("activation_4/Relu:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("conv2d_5/BiasAdd:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("batch_normalization_5/batchnorm/add_1:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("add_2/add:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("activation_5/Relu:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("conv2d_6/BiasAdd:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("batch_normalization_6/batchnorm/add_1:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("activation_6/Relu:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("conv2d_7/BiasAdd:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("batch_normalization_7/batchnorm/add_1:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("add_3/add:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("activation_7/Relu:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("conv2d_8/BiasAdd:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("batch_normalization_8/batchnorm/add_1:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("activation_8/Relu:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("conv2d_9/BiasAdd:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("batch_normalization_9/batchnorm/add_1:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("add_4/add:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("activation_9/Relu:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("conv2d_10/BiasAdd:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("batch_normalization_10/batchnorm/add_1:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("activation_10/Relu:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("conv2d_11/BiasAdd:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("batch_normalization_11/batchnorm/add_1:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("add_5/add:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("activation_11/Relu:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("conv2d_12/BiasAdd:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("batch_normalization_12/batchnorm/add_1:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("activation_12/Relu:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("conv2d_13/BiasAdd:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("batch_normalization_13/batchnorm/add_1:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("add_6/add:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("activation_13/Relu:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("conv2d_14/BiasAdd:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("batch_normalization_14/batchnorm/add_1:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("activation_14/Relu:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("conv2d_15/BiasAdd:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("batch_normalization_15/batchnorm/add_1:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("add_7/add:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("activation_15/Relu:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("conv2d_16/BiasAdd:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("batch_normalization_16/batchnorm/add_1:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("activation_16/Relu:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("conv2d_17/BiasAdd:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("batch_normalization_17/batchnorm/add_1:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("add_8/add:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("activation_17/Relu:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("conv2d_18/BiasAdd:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("batch_normalization_18/batchnorm/add_1:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("activation_18/Relu:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("conv2d_19/BiasAdd:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("batch_normalization_19/batchnorm/add_1:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("add_9/add:0", shape=(?, 17, 9, 16), dtype=float32)
Tensor("activation_19/Relu:0", shape=(?, 17, 9, 16), dtype=float32)
------------- policy -------------------
Tensor("conv2d_20/BiasAdd:0", shape=(?, 17, 9, 2), dtype=float32)
Tensor("activation_20/Relu:0", shape=(?, 17, 9, 2), dtype=float32)
Tensor("flatten/Reshape:0", shape=(?, 306), dtype=float32)
policy_output Tensor("activation_21/Softmax:0", shape=(?, 82), dtype=float32)
------------- policy -------------------
Tensor("conv2d_21/BiasAdd:0", shape=(?, 17, 9, 1), dtype=float32)
Tensor("activation_22/Relu:0", shape=(?, 17, 9, 1), dtype=float32)
Tensor("flatten_2/Reshape:0", shape=(?, 153), dtype=float32)
Tensor("dense_2/BiasAdd:0", shape=(?, 256), dtype=float32)
Tensor("activation_23/Relu:0", shape=(?, 256), dtype=float32)
Tensor("dense_3/BiasAdd:0", shape=(?, 1), dtype=float32)
Tensor("dense_3/BiasAdd:0", shape=(?, 1), dtype=float32)
```

```python
state = pickle.load(open("board1.pkl"))
state._create_neighbors_cache()
print util.pprint_board(state.board)
```

```text
   A B C D E F G H I 
 9 . . . . . . O . . 9
 8 . . . . . . O . O 8
 7 . . . . . . O . . 7
 6 . . O . X . . O X 6
 5 . . . . . . O . . 5
 4 X X X . . X . . . 4
 3 . X . . . . . . O 3
 2 . . . X X X . O . 2
 1 O . . . . . . . . 1
   A B C D E F G H I 
None
```

```python
res = net.eval_value_state(state)
print res
```

```text
0.803456
```

```python
import network, pickle, util, go

state = pickle.load(open("board1.pkl"))
#state.current_player = go.BLACK
print state.current_player
lm = state.get_legal_moves()
print len(lm), lm
res = net.eval_policy_state(state)
print res
```

```text
1
62 [None, (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 7), (0, 8), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 7), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 7), (2, 8), (3, 0), (3, 1), (3, 3), (3, 5), (3, 6), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 7), (4, 8), (5, 3), (5, 4), (5, 6), (5, 7), (5, 8), (6, 0), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (7, 0), (7, 1), (7, 2), (7, 6), (7, 8), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8)]
[0.00059019827, 0.0061528366, 0.023501551, 0.0051653204, 0.0041054208, 0.0014641138, 0.0019243082, 0.036704369, 0.00057243626, 0.031468783, 0.00075256237, 0.0016225742, 0.068846971, 0.0088369921, 0.0012060822, 0.012769492, 0.014729434, 0.012070517, 0.00035979468, 0.0079417937, 0.012058574, 0.0079989629, 0.002515546, 0.0044319183, 0.0018773929, 0.0097521804, 0.013427786, 0.047561217, 0.00046689392, 0.1153298, 0.00161595, 0.013073359, 0.0043753898, 0.11275286, 0.00070595962, 0.0031019931, 0.00082974677, 0.0015053105, 0.010339521, 0.0012516024, 0.028607352, 0.026982004, 0.0020673866, 0.0005492561, 0.009953157, 0.0016175937, 0.00051040156, 0.0047976626, 0.015361131, 0.0034852971, 0.0068298834, 0.0026259094, 0.00044995185, 0.00072519924, 0.010034629, 0.0040321173, 0.0015689885, 0.0047178767, 0.00049343513, 0.01525555, 0.01000932]
```









