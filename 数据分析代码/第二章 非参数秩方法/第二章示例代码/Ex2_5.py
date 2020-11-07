from scipy.stats import ks_2samp

a = [6.8, 3.1, 5.8, 4.5, 3.3, 4.7, 4.2, 4.9]
b = [4.4, 2.5, 2.8, 2.1, 6.6, 0.0, 4.8, 2.3]

# ks检验  检验指定的两个数列是否服从相同分布
# 也就是考察两组数据的现实效果是否有显著差异
statistic, p_value = ks_2samp(a, b)
print('statistic = ', statistic, ' pvalue = ', p_value)

# 取alpha=0.05,当alpha<p,则接受H0,认为效果差距不大
alpha = 0.05
if alpha < p_value:
    print('接受H0,在alpha=', alpha, '上,两组数据无显著差异.')
else:
    print('拒绝H0,alpha=', alpha, '上,两组数组有显著差异.')
