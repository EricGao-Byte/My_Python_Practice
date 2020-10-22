import itertools

# count会创建一个无限迭代器
natuals = itertools.count(1)
for n in natuals:
    print(n)

# cycle()会把传入的序列无线循环下去
cs = itertools.cycle('ABC')
# 字符串也是序列的一种
for c in cs:
    print(c)

# repeat()负责把一个元素无限重复下去,第二个参数限定重复次数
ns = itertools.repeat('A', 3)  # 重复A三次
for n in ns:
    print(n)

# 无限序列虽然可以无限迭代下去,但是我们通常用takewhile()等函数来判断截取出有限的序列
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
list(ns)

# chain()可以把一组迭代对象串联起来,形成更大的迭代器
for c in itertools.chain('ABC', 'XYZ'):
    print(c)

# groupby()把迭代器中相邻的重复元素挑出来放在一起
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))
# 若要忽略大小写,使用upper()转大写
for key, group in itertools.groupby('AaaBbBCcAaa', lambda c: c.upper()):
    print(key, list(group))

# 练习,计算圆周率
def pi(N):
    # 创建奇数数列
    odd = itertools.count(1, 2)
    # 取该序列前N项
    odd_N = list(itertools.takewhile(lambda x: x <= 2 * N - 1, odd))
    # 添加正负符号并用4除,例如:4/1 -4/3 4/5 -4/7
    sum = 0
    for n in range(N):
        if n % 2 == 0:
            odd_N[n] = 4 // odd_N[n]
        else:
            odd_N[n] = -4 / odd_N[n]
        sum = sum + odd_N[n]
        return sum
