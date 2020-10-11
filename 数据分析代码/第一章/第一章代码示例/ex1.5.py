import numpy as np

a = np.array([9.89,8.00,6.40,6.17,5.39,7.27,9.08,10.40,11.20,8.75,6.45,11.90,10.30,9.58,9.24,7.75,6.20,8.95,8.33])

# 求中位数
print(np.median(a))
# 求诸分位数
# interpotation为插值方法,当结果落到两个数据之间时,如何处理数据
print(np.percentile(a, (75,25,99,95,90,10,5,1), interpolation='midpoint'))
# 求极差
print(np.max(a)-np.min(a))
# 求四分位极差
Q = np.percentile(a, (75,25), interpolation='midpoint')
print(Q[0]-Q[1])
# 求三均值
M = np.median(a)
print(0.25*Q[1]+0.5*M+0.25*Q[0])