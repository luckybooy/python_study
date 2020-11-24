# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-24 10:59 AM

# 计算100～1000以内，各个数位上的数字的三次方之和 的数字有哪些
# 找水仙花【narcissus】数
"""
for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low**3 + mid**3 + high**3:
        print(num)
"""

"""
正整数的反转
"""

num = int(input('num = '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)

# 百钱百鸡 公的5元一只，母的3月一只，幼崽1月三只，现有100元，买100只，可以买到公、母、幼崽各多少只
for x in range(0, 22):
    for y in range(0, 33):
        z = 100 - x - y
        if 5*x + 3*y + z/3 == 100:
            print(x, y, z)