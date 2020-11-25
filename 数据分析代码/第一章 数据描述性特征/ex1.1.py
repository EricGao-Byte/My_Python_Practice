import numpy as np
import pandas as pd

a = np.array([12.38, 12.70, 12.96, 12.87, 12.66, 12.72, 12.74, 12.77, 13.06, 13.08])
# 求均值
print(np.mean(a))
# 求标准差
print(np.std(a))
# 求方差
print(np.var(a))
# 求变异系数=标准差/均值
print(np.std(a) / np.mean(a))

s = pd.Series(a)
# 求偏度
print(s.skew())
# 求峰度
print(s.kurt())
