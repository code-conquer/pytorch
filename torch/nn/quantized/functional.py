from torch._ops import ops

relu = ops.quantized.relu
sum_relu = ops.quantized.add_relu
