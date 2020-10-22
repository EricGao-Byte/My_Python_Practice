import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats

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

a = np.array(a)
# 做直方图并拟合正态分布曲线
sns.distplot(a, color="r", bins=30, kde=True)
plt.show()


# 经验分布函数图
def ecdf(a):  # 计算数据的ECDF值
    x = np.sort(a)
    y = np.arange(1, len(x) + 1) / len(x)
    return (x, y)


mu = np.mean(a)
sigma = np.std(a)

samples = np.random.normal(mu, sigma, 10000)

# Get the CDF of the samples and of the data
x, y = ecdf(a)
x_theor, y_theor = ecdf(samples)

# Plot the CDFs and show the plot
_ = plt.plot(x_theor, y_theor)
_ = plt.plot(x, y, marker='.', linestyle='none')
plt.margins(0.02)
_ = plt.xlabel('blood_index')
_ = plt.ylabel('ECDF')
plt.show()

# 做正态QQ图
stats.probplot(a, dist="norm", plot=plt)
plt.show()
