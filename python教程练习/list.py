classmate = ['gao', 'chuan', 'jin']
print(classmate)
len(classmate)  # 3
# 从头到尾
print(classmate[0])  # gao
print(classmate[1])  # chuan
print(classmate[2])  # jin
print(classmate[3])  # 报错
# 从尾到头
print(classmate[-1])  # jin
print(classmate[-2])  # chuan
print(classmate[-3])  # gao
print(classmate[-4])  # 报错

# list进行操作
# 列表尾部追加
classmate.append('nb')
print(classmate)
# 列表第一个元素后插入
classmate.insert(1, 'jack')
print(classmate)
# 列表尾部删除
classmate.pop()
print(classmate)
# 直接进行替换
classmate[1] = 'Sarath'
print(classmate)

# 不同于c语言,list中的元素还可以不同
L = ['Apple', 123, True]
print(L)
# list中还可以包含另外一个list
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(s)
# 还可以定义空白list
L = []
len(L)
