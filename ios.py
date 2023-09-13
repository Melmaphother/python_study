"""
a = input("Enter a number: ")
b = input("Enter another number: ")

print("aType: ", type(a))
print("bType: ", type(b))

a = float(a)
b = int(b)

result = a + b
print("resultValue: ", result)
print("resultType: ", type(result))
"""
import time  # 引入time模块

print(40, 'a', 50, 'a', 60, 'a', sep="|", end="\n")

Melmaphother = "Melmaphother"
school = "ustc"
print("%s已经%d岁了，他的学校是%s" % (Melmaphother, 19, school))

c = 10
print(hex(c), oct(c))

t1 = time.gmtime()  # gmtime()用来获取当前时间
t2 = time.gmtime()
print(t1 == t2)  # 输出True
"""
is 和 is not 代表两个变量是否引用同一个变量
判断两个对象的内存地址。如果内存地址相同，说明两个对象使用的是同一块内存，当然就是同一个对象
"""
print(t1 is t2)  # 输出False

age = 100
if age < 18:
    print("未成年")
elif age <= 60:
    print("青壮年")
else:
    print("老年")

a1 = 10
b1 = 5
max1 = a1 if a1 > b1 else b1
print("max1 = ", max1)

print(100 and 200)
print(45 and 0)
print("" or "python")
print(18.5 or "python")

num = 1
# 当 num 小于100时，会一直执行循环体
while num < 3:
    print("num=", num)
    # 迭代语句
    num += 1
print("循环结束!")
str1 = "PythonLearning"
for c in str1:
    print(c, end="")
print('\n')

result = 0
for i in range(1, 101):
    result += i
print(result)
