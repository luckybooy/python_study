# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-10 11:35 AM
def triangles(n):
    L=[1]
    while True:
        yield L
        L.append(0)
        L = [L[i-1] + L[i] for i in range (len(L))]


n = 0
for t in triangles(10):
    print(t)
    n = n + 1
    if n == 10:
        break