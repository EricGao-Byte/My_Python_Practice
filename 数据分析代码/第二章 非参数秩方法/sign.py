from scipy.special import comb


# method有两个选择 single表示单边 double表示双边
def sign_test(first, second, alpha, method="single"):
    if len(first) != len(second) or (method != "single" and method != "double"):
        print("两组数据维度不同，无法计算!\n")
        return None

    def get_Sn():
        pos = 0  # pos存储Sn
        n = len(first)  # n存储甲乙两组不相同的对数
        for i in range(len(first)):
            if first[i] > second[i]:
                pos += 1
            elif first[i] == second[i]:
                n -= 1
            else:
                continue
        return pos, n

    Sn, N = get_Sn()
    res = 0

    for i in range(Sn, N + 1):
        res += comb(N, i)

    res *= pow(2, -N)

    if method == "double":
        res *= 2
        print("双边检验p值为%f, alpha值为%f" % (res, alpha))
    else:
        print("单边检验p值为%f, alpha值为%f" % (res, alpha))

    if res < alpha:
        print("故拒绝原假设\n")
    else:
        print("故接受原假设\n")

    return None


first = [2.8, 3.9, 3.1, 2.9, 3.3, 2.6, 2.9, 3.4, 2.9, 2.9, 2.7, 2.6, 3.0, 3.3, 3.4, 2.7, 3.1, 2.7]
second = [2.5, 3.1, 3.3, 2.6, 3.1, 2.8, 2.7, 3.2, 2.7, 2.7, 2.5, 2.9, 3.4, 3.0, 3.2, 2.9, 2.8, 2.4]
alpha = 0.05
method = "single"

sign_test(first, second, alpha, method)
