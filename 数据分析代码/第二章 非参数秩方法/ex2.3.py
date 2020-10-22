# 多种处理方法比较的Kruskal-Wallis检验
from scipy import stats
# Kruskal-Wallis统计量的零分布
# stats.kruskal()

a=[164,190,203,205,206,214,228,257]
b=[185,197,201,231]
c=[187,212,215,220,248,265,281]
d=[202,204,207,227,230,276]
print(stats.kruskal(a,b,c,d))