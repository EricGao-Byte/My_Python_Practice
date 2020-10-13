# 计算圆面积函数示例
Pi = 3.141592653


def area_of_circle(r):
    if r < 0:
        return None
    else:
        return Pi * r * r


r = float(input("r: "))
s = area_of_circle(r)
print("area: ", s)


# 绝对值
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


a = input('x= ')
a = int(a)
print(my_abs(a))


# 定义一个什么都不做的空函数
# pass相当于一个占位符,能够让电脑正常运行起来
def nop():
    pass


# python中函数可以返回多个值
# 事实上返回值是一个tuple,仍然是单一数值
import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = x + step * math.sinh(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

# 练习
# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0ax
# 2
#  +bx+c=0 的两个解。
import math


def quadratic(a, b, c):
    delta = math.sqrt(b ** 2 - 4 * a * c)
    return (-b + delta) / (2 * a), (-b - delta) / (2 * a)


a = input('a: ')
b = input('b: ')
c = input('c: ')
a = int(a)
b = int(b)
c = int(c)
print(quadratic(a, b, c))
