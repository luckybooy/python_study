# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-09 10:48 AM
"""
list1 = list(range(1, 10))
print(list1)

for i in list1:
    print(i, end=' ')


print('\n'.join(['   '.join(('%dx%d = %2d') % (x, y, x*y) for x in range(1, y+1)) for y in range(1, 10)]))
"""

for i in range(1,10):
    for j in range(1, i+1):
        if j <= i:
            # print(j, '*',  i, '=', i*j,  end= '\t')
            print("{}x{}={}".format(j, i, j*i), end='\t')
    print()

