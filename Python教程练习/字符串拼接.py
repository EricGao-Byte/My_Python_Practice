age=12
name="ericdeamn"
print("name = %s"%name)
print("age = %d"%age)
# 多个字符串填充的情况
print("a = %s = %s"%("123","asdfg"))
# %3.5字符串长度限制在3-5个字符之间,默认匹配最长的情况
print("name = %3.5s"%name)
# %.2f表示浮点数后保留2位
print("num = %.2f"%1222.216213)
print("num1 = %.4f"%1123.13245)
# 格式化字符串,括号里为填充的变量
age = f'age = {name} {12}'
print(age)
welcome=f'欢迎 {name} 光临!'
print(welcome)
b=None
print(b)
print(type(age))