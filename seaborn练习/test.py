import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 切换到sns的默认配置
sns.set()

# 随机生成100个符合正态分布的数
x = np.random.randn(100)
# sns.kdeplot(x,shade=True,color='g',vertical=True)
y = np.random.randn(100)
# sns.kdeplot(x,y,shade=True,color='r',cbar=True)
# sns.displot(x,bins=50,color='g')


# 创建一个一行三列的画布
# fig, axes = plt.subplots(1, 3)
# sns.distplot(x, ax=axes[0])
# sns.distplot(x, hist=False, ax=axes[1])
# sns.distplot(x, kde=False, ax=axes[2])


# fig, axes = plt.subplots(1, 2)
# 分成20个区间
# sns.distplot(x, kde=False, bins=20, ax=axes[0])
# 以0,1,2,3为分割
# sns.distplot(x, kde=False, bins=[x for x in range(4)], ax=axes[1])


from scipy.stats import *

# 拟合标准正态分布
# sns.distplot(x, hist=False, fit=norm)

fig, axes = plt.subplots(1, 2)
sns.distplot(x, norm_hist=True, kde=False, ax=axes[0])
sns.distplot(x, kde=False, ax=axes[1])
plt.show()
