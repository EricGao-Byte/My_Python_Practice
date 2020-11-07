from scipy import stats


def sign_test(data1, data2, alpha, method='single'):
    if len(data1) != len(data2) or (method != 'single' and method != 'double'):
        print('两组数据维数不同,无法进行计算!\n')
        return None

    # 单总体分位数符号检验
    def sign_single_test(data, mu0):
        n = len(data)
        n_posi = 0
        for i in data:
            if i > mu0:
                n_posi += 1
        B = stats.binom(n, 0.5)
        p = B.cdf(n_posi)
        return p

    # 双总体分位数符号检验,根据p值判断
    def sign_double_test(data1, data2):
        n_posi = 0
        n = len(data1)
        for i in range(n):
            if (data1[i] > data2[i]):
                n_posi += 1
        # 根据二项分布求出p值
        B = stats.binom(n, 0.5)
        p = B.sf(n_posi - 1)
        return p

    if method == 'double':
        p = sign_double_test(data1, data2)
        p *= 2
        print('双边检验值p=%f,alpha=%f' % (p, alpha))
    else:
        p = sign_double_test(data1, data2)
        print('单边检验值p=%f,alpha=%f' % (p, alpha))

    if p < alpha:
        print('拒绝原假设\n')
    else:
        print('接受原假设\n')


# 对成对分组设计下两种处理方法的比较
# 符号检验
# 以书P65为例
class Solution:
    def solve(self):
        data1 = [2.8, 3.9, 3.1, 2.9, 3.3, 2.6, 2.9, 3.4,
                 2.9, 2.9, 2.7, 2.6, 3.0, 3.3, 3.4, 2.7, 3.1, 2.8]
        data2 = [2.5, 3.1, 3.3, 2.6, 3.1, 2.8, 2.7, 3.2,
                 2.7, 2.7, 2.5, 2.9, 3.4, 3.0, 3.2, 2.9, 2.8, 2.4]
        alpha = 0.05
        method = 'single'
        # 双总体符号检验,根据p值判断
        sign_test(data1, data2, alpha, method)


s = Solution()
s.solve()
