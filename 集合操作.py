# 集合的使用
list1 = {1,2,3,7}
list2 = {1,2,3,9}

# 交集
print(list1.intersection(list2))
# 并集
print(list1.union(list2))
# 差集
print(list1.difference(list2)) # list1里面有list2中没有的
print(list2.difference(list1)) # list2里面有list1中没有的
# 子集
print(list1.issubset(list2))   # list1是list2的子集吗？
# 父级
print(list1.issuperset(list2))
# 对称差集
print(list1.symmetric_difference(list2))
print(list1 ^ list2)
# 添加
list1.add(2222)
print(list1)
# 修改
list1.update([2,3,4,5,6])
print(list1)
# 判断集合长度
print(len(list1))
# 删除
list1.remove(2)
print(list1)
# 测试x是否是在list1中
x in list1
# 测试x是否不是在list1中
x not in list1

# 交集、并集、差集、子集、父级、对称差集、添加、修改、删除
print(
list1.intersection(list2),
list1.union(list2),
list1.difference(list2),
list1.issubset(list2),
list1.issuperset(list2),
list1.symmetric_difference(list2),
list1.add(11),
list1.remove(22),
list1.update([11,22]),
)
