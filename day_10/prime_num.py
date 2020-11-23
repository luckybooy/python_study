# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-23 11:30 AM

# 判断一个数是不是素数
# 素数：只能被1和本身整除的大于1的整数叫素数
from math import sqrt

num = int(input("请输入一个正整数:"))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print("%d是素数" % num)
else:
    print("%d不是素数" % num)
