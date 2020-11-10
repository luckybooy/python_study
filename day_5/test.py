# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-10 11:42 AM
"""
L=[1]
L = [L[i - 1] + L[i] for i in range(len(L))]
print(L)
"""

gen = (x * x for x in range(10))

for num in gen:
    print(num)


