# set为一组key的集合,由于key不能重复,因此set中没有重复的key
s = set([1, 2, 3])
print(s)  # {1,2,3}

# 重复元素在set中会被过滤
s = set([1, 1, 2, 2, 3, 3, ])
print(s)  # {1,2,3}

# 添加元素到set中
s.add(4)
print(s)

# 删除元素
s.remove(4)
print(s)

# 数学求并集和交集
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s1 & s2  # {2,3}
s1 | s2  # {1,2,3,4}


