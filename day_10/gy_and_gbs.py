# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-23 1:32 PM

# descprition :输入两个数，计算他们的最大公约数和最小公倍数
x = int(input("x = "))
y = int(input("y = "))
# 如果x > y，交换x,y的位置
if x > y:
    # 下边的形式就是将y的值赋给x,将x的值赋给y
    x, y = y, x

    # 从两个数中较小的开始，进行递减循环

for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print("%d和%d的最大公约数是%d" % (x, y, factor))
        print("%d和%d的最小公倍数是%d" % (x, y, x * y // factor))
        break
