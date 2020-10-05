# 特殊的 python中字符串进行比较时,依据Unicode编码逐位进行比较
a = 'abcd'
b = 'abad'
result = a > b # c>a True
print(result)

# is 比较是否为同一个对象,即比较id是否相等
a=10
b=10
result = a is b  # a和b指向同一个对象
print(result)
b=100
result = a is not b
print(result)


