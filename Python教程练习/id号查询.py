a = 10
print(id(a))
a = "100"  # 每次值改变都会改变id,因为内存改变了,id事实上就是内存地址
print(id(a))
