# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-25 12:16 AM
import math
"""
找出1～9999之间的完美数
完美数：一个数的除了本身外所有因子之和等于这个数
如：6 因子(factor)[3,2,1] 3 + 2 + 1 = 6
"""
for num in range(1, 10000):
    res = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            res += factor
            if factor > 1 and num // factor != factor:
                res += num // factor
    if res == num:
        print(num, end=' ')