import numpy as np

# a = np.array([1, 2, 3])
# print(a)
# b = np.array([[1, 2], [3, 4]])
# print(b)
# a = np.array([1, 2, 3, 4, 5], ndmin=3)
# print(a)
# a = np.array([1, 2, 3], dtype=complex)
# print(a)

# # 维度检测ndim
# a = np.arange(24)
# # n为1维度
# print(a.ndim)
# # 改为3维度
# b = a.reshape(2, 4, 3)
# print(b.ndim)

# 数据大小检测shape,调整数组大小
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)
# 调整数组大小为3行2列
a.shape = (3, 2)
print(a)

