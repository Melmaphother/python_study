"""
同一集合中，只能存储不可变的数据类型，包括整形、浮点型、字符串、元组，
无法存储列表、字典、集合这些可变的数据类型
"""
""" 集合不能有重复元素 """
a = {1, 'c', 1, (1, 2, 3), 'c'}
print(a)

set1 = set("c.biancheng.net")
print(set1)

# 创建空集合只能使用set()，不能使用set = {}，会解释为一个字典

# 增
# # add()方法
"""
使用 add() 方法添加的元素，只能是数字、字符串、元组或者布尔类型（True 和 False）值，
不能添加列表、字典、集合这类可变的数据
"""
set2 = {1, 2, 3}
set2.add((1, 2))
print(set2)
# 删
# # remove(elem) 和 discard(elem)
"""remove()不存在会报错，discard()不会"""

# 集合之间的交并补
set3 = {1, 2, 3}
set4 = {3, 4, 5}
print(set3 & set4)
print(set3 | set4)
print(set3 - set4)
print(set3 ^ set4)  # 类似异或

# 访问set中的元素
"""
由于集合中的元素是无序的，
因此无法向列表那样使用下标访问元素。
Python 中，访问集合元素最常用的方法是使用循环结构，将集合中的数据逐一读取出来
"""
for elem in set1:
    print(elem, end="")

# set中的方法
""" 可以使用函数dir()看有哪些方法 """
print(dir(set))

set5 = set3.intersection(set4)  # 取交集给set5
print(set5)
set3.intersection_update(set4)  # 取交集更新给set3
print(set3)
print(set3.isdisjoint(set4))  # 是否没有交集，有交集返回False，没有返回True
print(set3.issubset(set4))  # 是否是子集
print(set3.issuperset(set4))  # set4是否是set3的子集
set6 = set3.union(set4)  # 取并集给set6
print(set6)
set3.update([1, 2, 3, 4, 5])  # 添加列表或集合中的元素到 set3
print(set3)

# 关于frozenset
"""
当集合的元素不需要改变时，我们可以使用 fronzenset 替代 set，这样更加安全。
有时候程序要求必须是不可变对象，这个时候也要使用 fronzenset 替代 set。比如，字典（dict）的键（key）就要求是不可变对象。
"""
s = {'Python', 'C', 'C++'}
fs = frozenset(['Java', 'Shell'])
s_sub = {'PHP', 'C#'}
# #向set集合中添加frozenset
s.add(fs)
print('s =', s)
# #向为set集合添加子set集合，不合法
# s.add(s_sub)
# print('s =', s)
