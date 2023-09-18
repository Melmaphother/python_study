# 字符串索引
str1 = "我来自中国科学技术大学"
# #取索引区间为[0,2]之间（不包括索引2处的字符）的字符串
print(str1[:2])
# #隔 1 个字符取一个字符，区间是整个字符串
print(str1[::2])
# #取整个字符串，此时 [] 中只需一个冒号即可
print(str1[:])

# 字符串基本方法之最大最小以及排序
str2 = "Melmaphother.com"
# # 找出最大的字符
print(max(str2))
# # 找出最小的字符
print(min(str2))
# # 对字符串中的元素进行排序
print(sorted(str2))

# 字符串拼接
# # 字符串常量的拼接
"""   "str1""str2"   """
print("I"" am ""Melmaphother")
# # 字符串变量的拼接
print(str1 + str2)
# # 字符串转化
"""
str() 和 repr() 函数虽然都可以将数字转换成字符串，但它们之间是有区别的：
str() 用于将数据转换成适合人类阅读的字符串形式。
repr() 用于将数据转换成适合解释器阅读的字符串形式（Python 表达式的形式），
       适合在开发和调试阶段使用；如果没有等价的语法，则会发生 SyntaxError 异常。
"""

# string中的方法
# # 长度
print(len(str2))  # 获取字符串的长度
print("str1 len", len(str1))
print("str1 len(UTF-8)", len(str1.encode()))  # 默认 'UTF-8'
print("str1 len(GBK)", len(str1.encode('GBK')))  # 按某编码进行重新编码

# # 字符串split
"""
    str.split(sep,maxsplit)
    str：表示要进行分割的字符串；
    sep：用于指定分隔符，可以包含多个字符。此参数默认为 None，表示所有空字符，包括空格、换行符“\n”、制表符“\t”等。
    maxsplit：可选参数，用于指定分割的次数，最后列表中子串的个数最多为 maxsplit+1。如果不指定或者指定为 -1，则表示分割次数没有限制。

"""
print(str2.split('e'))
print(type(str2.split('e')))  # list

# # 字符串join
"""
    newstr = str.join(iterable)     iterable : 可迭代的
    split的逆过程
    newstr：表示合并后生成的新字符串； 
    str：用于指定合并时的分隔符；
    iterable：做合并操作的源字符串数据，允许以列表、元组等形式提供
"""
dire = '', 'usr', 'bin', 'env'  # 也可以用 ('', 'usr', 'bin', 'env')
print(type(dire))  # tuple
print('/'.join(dire), type('/'.join(dire)))  # str

# # 统计字符串个数count
"""
str.count(sub[,start[,end]])
"""
print(str2.count('e'))

# # 查找字串find和rfind

"""
str.find(sub[,start[,end]])
找不到返回-1，找到返回第一次找到的索引
rfind从右向左索引
"""
print(str2.find('el'))
print(str2.rfind('el'))

# # 字符串输出左、右对齐和居中 ljust rjust center
S1 = 'http://Melmaphother.github.io'
S2 = 'http://Melmaphother'
print(S1.ljust(35, '-'))
print(S2.ljust(35, '-'))
print(S1.rjust(35, '-'))
print(S2.rjust(35, '-'))
print(S1.center(35, '-'))
print(S2.center(35, '-'))


# # 是否以某串开头或结尾
print('e' in S1)
print(S1.startswith('http'))
print(S1.endswith('io'))

# # 字符串大小写转换
"""
    返回新的字符串
    str.title()  将字符串中每个单词的首字母转为大写，其他字母全部转为小写
    str.lower()  将字符串中的所有大写字母转换为小写字母
    str.upper()  将字符串中的所有小写字母转换为大写字母
"""


# # 字符串去除字符串中的空格或其他字符

"""
    strip()：删除字符串前后（左右两侧）的空格或特殊字符。
    lstrip()：删除字符串前面（左边）的空格或特殊字符。
    rstrip()：删除字符串后面（右边）的空格或特殊字符。
"""

trip1 = '\n\nssss\n\n'
print(trip1.strip())
print(trip1.lstrip())
print(trip1.rstrip())

