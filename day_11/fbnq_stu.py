# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-24 2:35 PM

# 计算斐波那契数列的前二十位数
a = 0
b = 1

for i in range(20):
    a, b = b, a + b
    print(a, end=',')
