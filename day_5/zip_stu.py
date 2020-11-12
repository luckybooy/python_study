# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-10 5:30 PM
a = ['xiaoming', 'lihua', 'lincong']
b = ['beijing', 'shanghai', 'tianjin']
c = ['18', '20', '22', '25']

#dict1 = dict(zip(a, b, c))
#print(dict1)

dict1 = zip(a, b, c)
for aa in dict1:
    print(aa)
#print(dict1)