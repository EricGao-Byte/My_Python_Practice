import numpy as np
from scipy.stats import kstest
from scipy.stats import chi2_contingency
import numpy as np
from scipy.stats import shapiro

a = [74.3, 78.8, 68.8, 78.0, 70.4, 80.5, 80.5, 69.7, 71.2, 73.5
    , 79.5, 75.6, 75.0, 78.8, 72.0, 72.0, 72.0, 74.3, 71.2, 72.0
    , 75.0, 73.5, 78.8, 74.3, 75.8, 65.0, 74.3, 71.2, 69.7, 68.0
    , 73.5, 75.0, 72.0, 64.3, 75.8, 80.3, 69.7, 74.3, 73.5, 73.5
    , 75.8, 75.8, 68.8, 76.5, 70.4, 71.2, 81.2, 75.0, 70.4, 68.0
    , 70.4, 72.0, 76.5, 74.3, 76.5, 77.6, 67.3, 72.0, 75.0, 74.3
    , 73.5, 79.5, 73.5, 74.7, 65.0, 76.5, 81.6, 75.4, 72.7, 72.7
    , 67.2, 76.5, 72.7, 70.4, 77.2, 68.8, 67.5, 67.5, 67.3, 72.7
    , 75.8, 73.5, 75.0, 73.5, 73.5, 73.5, 72.7, 81.6, 70.3, 74.3
    , 73.5, 79.5, 70.4, 76.5, 72.7, 77.2, 84.3, 75.0, 76.5, 70.4]

data = a
# w检验
stat, p = shapiro(data)
print("stat：%f" % stat, "p value：%f" % p)

# 关于正态分布假设的Kolmogorov-Smirnov检验
# 输出结果中第一个为统计数，第二个为P值，P值大于0.05，很可能为正态分布
print(kstest(a, 'norm'))

# 卡方检验
kf_data = np.array(a)
kf = chi2_contingency(kf_data)
print('chisq-statistic=%.4f, p-value=%.4f, df=%i expected_frep=%s' % kf)
