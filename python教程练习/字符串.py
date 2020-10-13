# ord()获取字符的整数表述
ord('A')
ord('中')
# chr()把编码转换为对应的字符
chr(66)
chr(25991)

# str类型
x = 'ABC'
print(len(x))
# bytes类型,每个字符占据1字节
x = b'ABC'
print(len(x))
# 中文字符通常一个会占用三个字节,英文字符一个只会占用一个字符
x = ('中文'.encode('utf-8'))
print(len(x))
print('中文'.encode('gb2312'))
print('中文'.encode('utf-8'))


# 将bytes变为str需要decode()函数
b'ABC'.decode('ascii')
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

# 格式化输出代码%f 浮点数 %x 十六进制整数
'hello %s' % 'world'
'hi %s you have $%d' % ('gao', 10000)
'%2d-%02d' % (3, 1)
'%.2f' % 3.14134321  # 小数点后保留两位
# %为普通字符的情况
'growth rate: %d %%' % 7
# 另外一种格式化字符的方法使用format()函数,依次传入占位符{0},{1}...
'hello {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
# 最后一种格式化字符串的方法使用以f开头的字符串,用变量名进行替换
r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')

