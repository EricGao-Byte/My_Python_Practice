# not 相当于C中的!符号,进行取反操作
a = True
a = not a
print(a)

# and
a = True
b = False
c = a and b  # 且运算
print(c)

# or
a = True
b = False
c = a or b  # 或运算
print(c)

# 数字进行逻辑运算时会转换为bool值,最终返回原值
#  与运算找false,第一个值为false时,则直接返回第一个值,否则返回第二个值
result = 1 and 2
print(result)
result = 0 and 2
print(result)
result = 2 and 0
print(result)
result = 0 and None
print(result)
#  或运算和与运算相反
result = 1 or 2
print(result)
result = 2 or 0 
print(result)
result = 0 or 2
print(result)
