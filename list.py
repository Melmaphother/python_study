li = ['Python', 'C++', 'Java']
# 追加元素
li.append('PHP')
print(li)

li.append(['Ruby', 'SQL'])
print(li)

"""extend是逐个加，append是作为一个整体进行加和"""
li.extend(['Ruby', 'SQL'])
print(li)

del li[4:]
print(li)

nums = [40, 36, 89, 2, 36, 100, 7]
# 在4个位置插入元素
nums[4: 4] = [-77, -52.5, 999]
print(nums)
# 修改第四个位置的值
nums[4: 5] = ['a', 'b', 'c']
print(nums)
# 使用切片语法时也可以指定步长（step 参数），但这个时候就要求所赋值的新元素的个数与原有元素的个数相同
# 否则会报错
nums2 = [40, 36, 89, 2, 36, 100, 7]
# 步长为2，为第1、3、5个元素赋值
nums2[1: 6: 2] = [0.025, -99, 20.5]
"""这样写会报错：nums2[1: 6 : 2]=[0.025, -99, 20.5, 1]"""
# nums2[1: 6: 2] = [0.025, -99, 20.5, 1]
print(nums2)

nums3 = [1, 2, 3, 4, 5, 6, 7]
val = 1
if nums3.count(val):
    print("有%d这个数" % val, "他的索引是:%d" % nums3.index(1))
else:
    print("没有这个数")
