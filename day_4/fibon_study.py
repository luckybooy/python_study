# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-09 1:41 PM
def fun_fibon(n):
    a = b =1
    for i in range(n):
        yield a
        a ,b = b, a+b



for x in fun_fibon(100):
    print(x, end=' ')