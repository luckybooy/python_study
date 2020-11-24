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
