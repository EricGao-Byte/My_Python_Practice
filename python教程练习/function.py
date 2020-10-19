import math

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


nop()


# python中函数可以返回多个值
# 事实上返回值是一个tuple,仍然是单一数值


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


# 可变参数
# 若参数个数不确定,可以将参数利用list或tuple传入达到参数可变的效果
# 以下是一般情况
def calc(numbers):
    sum = 0
    for number in numbers:
        sum += number * number
    return sum


# 利用list传入
print(calc([1, 2, 3]))
print(calc([1, 234, 45, 34]))
# 无法传入0个参数
print(calc())


# 可变参数的写法,在参数前面加*号
# 事实上可变参数在传入时,系统会自动为可变参数创建一个tuple
def calc_var(*numbers_var):
    sum = 0
    for number_var in numbers_var:
        sum += number_var * number_var
    return sum


# 可以传入任意数量参数
print(calc_var(1, 2, 3))
print(calc_var(1, 234, 45, 34))
# 可以传入0个参数
print(calc_var())

# 若已经有一个list或一个tuple,如何使用可变参数?
nums = [1, 2, 3]
print(calc_var(nums[0], nums[1], nums[2]))


# 关键字参数
# 将传入的关键字和值在函数内部组装为dict,注意kw为赋值,改变kw不改变外部dict的真实值
# 下面的例子中**kw即为关键字参数
def person(name, age, **kw):
    # 关键字检查
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, 'age:', age, 'other:', kw)


# 只传入必选参数
print(person('Michael', 30))
# 传入任意个数关键字参数
person('bob', 35, city='Beijing')
person('adam', 45, gender='M', job='Engineer')
# 类似于可变参数,也可以先在函数外部先将dict组装好
extra = {'city': 'beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])


# 命名关键字参数
# 用于需要限制关键字参数的名字的情况
# 例如: 只接受city和job作为关键字参数
# 且命名关键字可以有缺省值
def person_only(name, age, *, city='beijin', job):
    print(name, age, city, job)


print(person_only('jack', 24, job='engineer'))

