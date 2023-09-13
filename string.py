str1 = "C语言中文网"
# 取索引区间为[0,2]之间（不包括索引2处的字符）的字符串
print(str1[:2])
# 隔 1 个字符取一个字符，区间是整个字符串
print(str1[::2])
# 取整个字符串，此时 [] 中只需一个冒号即可
print(str1[:])


str2 = "c.biancheng.net"
# 找出最大的字符
print(max(str2))
# 找出最小的字符
print(min(str2))
# 对字符串中的元素进行排序
print(sorted(str2))
