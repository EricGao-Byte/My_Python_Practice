# dic全称dictionary,也叫map,使用键值(key-value)存储
# 查询速度快
d = {'gao': 95, 'chuan': 75, 'jin': 85}
print(d['gao'])

# 除了初始化指定为,还可以通过key放入
# 需要注意的是dict内部存放的顺序与key放入顺序无关
print(d)
d['gao'] = 67
print(d)

# 判断key是否存在
'Thomas' in d  # False
# 返回None或者返回自己指定的数字
d.get('Thomas')
d.get('Thomas', -1)

# 和list比较，dict有以下几个特点：
#
# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。
# 而list相反：
#
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。

# 需要注意的是key一定要是不可变对象,比如字符串 整数
# 这是因为key的位置计算算法为哈希算法
key = [1, 2, 3]
d[key] = 'a list'  # TypeError: unhashable type: 'list'
