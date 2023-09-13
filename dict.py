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

