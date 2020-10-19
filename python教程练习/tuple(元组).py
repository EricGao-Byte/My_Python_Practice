# tuple 元组 也叫有序数列
classmate = ('gao', 'bob', 'jin', 1)
# 一旦初始化就无法修改,其中的元素也无法赋值为其他值
print(classmate)

# tuple陷阱
t = (1, 2)
print(t)
t = ()
print(t)
# 当定义单元素的tuple时,会出现问题
t = (1)
print(t)
# 正确的定义方式
t = (1,)
print(t)

# 元素可变的tuple
t = ('a', 'b', ['A', 'B', 'C'])
print(t)
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
