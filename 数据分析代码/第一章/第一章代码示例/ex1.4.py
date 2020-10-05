import numpy as np

a = (5, 3, 11, 3, 1, 7, 8)

# a为源数据，percentile内的元组为要求的第N分位数，比如75为0.75分位数
print(np.percentile(a, (75, 25, 99, 95, 90, 10, 5, 1), interpolation='midpoint'))
