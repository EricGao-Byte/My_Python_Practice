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
sns.distplot(a, color='r', bins=30, kde=True)
plt.show()


# 经验分布函数图
# 定义经验分布函数
def ecdf(a):
    x = np.sort(a)
    y = np.arange(1, len(x) + 1) / len(x)
    return (x, y)


mu = np.mean(a)
sigma = np.std(a)
# 生成1000个符合正态分布的数据,均值为mu,标准差为sigma
samples = np.random.normal(mu, sigma, 1000)
x, y = ecdf(a)  # 实验值
x_theor, y_theor = ecdf(samples)  # 理论值
# 画图
_ = plt.plot(x_theor, y_theor)
_ = plt.plot(x, y, marker='.', linestyle='none')
plt.margins(0.02)
_ = plt.xlabel('blood_index')
_ = plt.ylabel('ECDF')
plt.show()

# 做正态QQ图
stats.probplot(a, dist="norm", plot=plt)
plt.show()
