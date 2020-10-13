# 默认参数n=2
def power(x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s


# !!!!默认参数一定要指向不变对象
def add_end(L=[]):
    L.append('END')
    return L


add_end()  # 每次运行之后都会增加一个END输出,这与实际不符合
