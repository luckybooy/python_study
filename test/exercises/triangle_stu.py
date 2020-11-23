# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-23 5:50 PM
for i in range(6):
    print("*"*i, end='\n')


row = int(input("请输入要打印的行数："))
print("左对齐三角形")
# 左对齐
for i in range(row):
    for _ in range(i+1):
        print('*', end='')
    print()

print("右对齐三角形")
# 右对齐三角形
for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()


print("居中三角形")
# 居中对齐
for i in range(row):
    for j in range(row - i - 1):
        print(' ', end='')
    for j in range(i * 2 + 1):
        print('*', end='')
    print()

