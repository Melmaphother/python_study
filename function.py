"""
python函数
"""
import math

# python 的值传递
"""
    Python 中，根据实际参数的类型不同，函数参数的传递方式可分为 2 种，分别为值传递和引用（地址）传递：
    值传递：适用于实参类型为不可变类型（字符串、数字、元组）；
    引用（地址）传递：适用于实参类型为可变类型（列表，字典）；

"""


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(1, 2, 3, 1)
print(2 ** 3)
