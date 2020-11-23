# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-23 1:47 PM

x = int(input("x = "))
y = int(input("y = "))

if x > y:
    x, y = y, x
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print("%d和%d的最大公约数是%d" % (x, y, factor))
        print("%d和%d的最小公倍数是%d" % (x, y, x * y // factor))
        break




a = 5
b = 2
print(a/b)   # 2.5 '/' 就表示 除
print(a//b)  # 2 "//"向下取整 表示 整除

for i  in range(6):
    print("*"*i)