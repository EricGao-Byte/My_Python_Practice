import pandas as pd
import numpy as np

# series时一个一维数组,基于numpy的ndarray结构
# 默认用0-n-1为index,也可自己指定index

# series的创建
# 格式: pd.Series([list], index=[list])
s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'f', 'e'])
print(s)

# series取值
# 取值操作类似数组
v = np.random.random_sample(50)
s = pd.Series(v)
s1 = s[[3, 13, 23, 33]]
s2 = s[3:13]
s3 = s[43]
print("s1", s1)
print("s2", s2)
print("s3", s3)
