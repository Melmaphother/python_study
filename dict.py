"""
字典（dict）是一种无序的、可变的序列，
它的元素以“键值对（key-value）”的形式存储。
相对地，列表（list）和元组（tuple）都是有序的序列，它们的元素在底层是挨着存放的。

字典类型是 Python 中唯一的映射类型。
相当于C++中的 unordered_map 对象
"""
scores = {'数学': 95, '英语': 92, '语文': 84}
print(scores)

print(scores.get('生物', '该项不存在'))

""" 关于创建字典 """
""" 1. fromkeys常用于初始化字典  """
keys = [1, 2, 3]
dict1 = dict.fromkeys(keys, 0)
print(dict1)

"""2. 向 dict() 函数传入列表或元组，而它们中的元素又各自是包含 2 个元素的列表或元组，其中第一个元素作为键，第二个元素作为值。"""
demo1 = [['one', 1], ['two', 2], ['three', 3]]
demo2 = (['one', 1], ['two', 2], ['three', 3])
demo3 = (('one', 1), ('two', 2), ['three', 3])
demo4 = [('one', 1), ('two', 2), ('three', 3)]

demo = dict(demo1)
print(demo)
"""3. 通过应用 dict() 函数和 zip() 函数，可将前两个列表转换为对应的字典。"""
keys2 = ['one', 'two', 'three']
value1 = ['1', '2', '3']
dict2 = dict(zip(keys2, value1))
print(dict2)

"""4. 创建空的字典 """
dict3 = dict()
print(dict3)

""" 字典中各元素的键都只能是字符串、元组或数字，不能是列表。列表是可变的，不能作为键。 """

""" 字典中元素的处理 """
# 插入元素
# # 直接给不存在的 key 赋值即可
dict4 = {'one': 1, 'two': 2, 'three': 3}
print(dict4)
dict4['four'] = 4
print(dict4)
# # 修改元素
dict4['four'] = 5
print(dict4)
# # 删除元素
del dict4['four']
print(dict4)
# # 寻找字典中是否存在某个key
print('four' in dict4)

# 字典方法
# # key() value()
print(dict4.keys())
print(dict4.values())
# # items()
list3 = []
for key, value1 in dict4.items():
    list3.append(value1)
    print(key, ':', value1)
print(list3)

"""
返回可遍历的(键, 值) 元组列表。
<class 'dict_items'>
"""
print(type(dict4.items()))

# # copy()的深浅拷贝问题
a = {'one': 1, 'two': 2, 'three': [1, 2, 3]}
b = a.copy()
# 向 a 中添加新键值对，由于b已经提前将 a 所有键值对都深拷贝过来，因此 a 添加新键值对，不会影响 b。
a['four'] = 100
print(a)
print(b)
# 由于 b 和 a 共享[1,2,3]（浅拷贝），因此移除 a 中列表中的元素，也会影响 b。
a['three'].remove(1)
print(a)
print(b)


# # update()
""" 如果被更新的字典中己包含对应的键，那么原 value 会被覆盖；如果被更新的字典中不包含对应的键值对，则该键值对被添加进去。"""

dict5 = {'one': 1, 'two': 2, 'three': 3}
dict5.update({'one': 4.5, 'four': 5})
print(dict5)

# # pop() 和 popitem()
"""
dict_name.pop(key)
dict_name.popitem()

"""
dict5.pop('one')
print(dict5)
dict5.popitem()
print(dict5)
""" 虽然字典是一种无须的列表，但键值对在底层也是有存储顺序的，popitem() 总是弹出底层中的最后一个 key-value """

# # setdefault()
""" 返回键对应的值，不存在则返回 defaultvalue """

print(dict5.setdefault('two'))
print(dict5.setdefault('one'))

