from scipy import stats
import math


# 对成对分组设计下两种处理方法的比较
# 符号检验
# 以书P65为例
class Solution:
    def solve(self):
        data1 = [2.8, 3.9, 3.1, 2.9, 3.3, 2.6, 2.9, 3.4,
                 2.9, 2.9, 2.7, 2.6, 3.0, 3.3, 3.4, 2.7, 3.1, 2.8]
        data2 = [2.5, 3.1, 3.3, 2.6, 3.1, 2.8, 2.7, 3.2,
                 2.7, 2.7, 2.5, 2.9, 3.4, 3.0, 3.2, 2.9, 2.8, 2.4]
        # 双总体符号检验,根据p值判断
        sign_double_test_one(data1, data2)


# 单总体分位数符号检验
def sign_single_test(data, mu0):
    n = len(data)
    n_posi = 0
    for i in data:
        if i > mu0:
            n_posi += 1
    B = stats.binom(n, 0.5)
    p = B.cdf(n_posi)
    print(p)


# 双总体分位数符号检验,根据p值判断
def sign_double_test_one(data1, data2):
    n_posi = 0
    n = len(data1)
    for i in range(n):
        if (data1[i] > data2[i]):
            n_posi += 1
    # 根据二项分布求出p值
    B = stats.binom(n, 0.5)
    p = B.sf(n_posi - 1)
    print(p)


# 双总体分位数符号检验,根据临界值判断
def sign_double_test_two(data1, data2, a):
    n_posi = 0
    n = len(data1)
    for i in range(n):
        if (data1 > data2):
            n_posi += 1
    B = stats.binom(n, 0.5)
    c1 = B.ppf(a / 2.0)
    c2 = B.ppf(1 - a / 2.0)
    if (B.ppf(c1) > a / 2.0):
        c1 = c1 - 1
        c2 = c2 + 1

    print(c1, c2)


s = Solution()
answer = s.solve()
