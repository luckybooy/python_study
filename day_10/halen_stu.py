# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-23 10:37 AM

import math
# 输入三个数，看是否能构成一个三角形，能的话计算出其周长和面积

a = int(input("请输入三角形的第一条边："))
b = int(input("请输入三角形的第二条边："))
c = int(input("请输入三角形的第三条边："))

if ((a + b > c) and (a+c>b)and(b+c >a)):
    primeter = a + b +c

    pp = primeter / 2
    #海伦公式：三角形的面积=(周长*(周长-边1)*(周长-边2)*(周长-边3) )** 0.5
    area = (pp*(pp-a)*(pp-b)*(pp-c))**0.5
    print("该三角形的周长为：{},面积为:{}".format(primeter, area))
else:
    print("不能组成三角形")