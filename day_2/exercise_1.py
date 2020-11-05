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
        print("{}x{}={}\t".format(j, i, i*j), end='')
    print()



#判断是否是闰年
YEAR = int(input("请入一个年份："))
print(type(YEAR))
if(YEAR%400 ==0 or (YEAR %4==0 and YEAR%100 != 0)):
    print("{0}年是闰年".format(YEAR))
else:
    print("{0}年不是闰年".format(YEAR))