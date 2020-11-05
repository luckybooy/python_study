# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-05 2:29 PM
# 乘法口诀
result = 1
for i in range(1, 10):
    for j in range(1, 10):
        if j <= i:
            print("{}x{}={}\t".format(j, i, j*i), end='')
    print()

print("*********************separator********************")

for i in range(1, 10):
    for j in range(1, i+1):
        print("{}x{}={}\t".format(i, j, i*j), end='')
    print()