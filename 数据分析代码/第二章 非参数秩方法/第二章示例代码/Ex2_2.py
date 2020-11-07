from scipy.stats import ranksums
from scipy.stats import ks_2samp

a = [18, 24, 25, 27, 30, 35]
b = [20, 21, 28, 32, 34, 38, 40]

# a=[3,5,7,9,10]
# b=[1,2,4,6,8]

# a=[4,6,7,9,10]
# b=[1,2,3,5,8]

# 秩和检验
print(ranksums(a, b))
# ks检验  检验指定的两个数列是否服从相同分布
print(ks_2samp(a,b))