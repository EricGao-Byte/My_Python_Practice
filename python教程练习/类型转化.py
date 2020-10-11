# 有四种转换函数int() float() str() bool()
# 对于bool() 只有0,None,''会转换为False
# 对于str() 不是整型无法转换
a=True
print(type(a))
a=str(a)
print(type(a))
b=100
print(type(b))
float(b)  # 类型转换不会影响到原来变量的类型
print(type(b))