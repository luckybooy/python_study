# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-05 4:07 PM
# 定义一个函数
"""
格式：
def 函数名(参数列表):  ":" 冒号很重要 表示函数体的开始
    函数体
    return 返回值(没有的话默认返回None)
"""
def sum (num1, num2):
    res = num1 + num2
    return res

print(sum(1, 3))

def calcu (num1, num2):
    if not(isinstance(num1, (int, float))) and isinstance(num2,(int, float)):
        print("invalid parameters")
    return num1 + num2

print(calcu(3, 5))

# 无效参数事例
print(calcu('23', 5))