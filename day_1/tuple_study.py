# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-04 2:42 PM
# description：元组学习 tuple

""" 元组被初始化后就不能被改变
所以就没有append，insert等方法
tuple 正是由于他的不可变性，所以安全可靠
能用tuple时就不用list
"""
phone = ('iphone', 'huawei', 'xiaomi', 'appo', 'vivo')
print(phone)
print(phone[1])
num = (123)
print(type(num))
num1 = (123,)       #创建只有一个元素的元组的时候需要在元素后添加一个逗号
print(type(num1))
num2 = ('123')
print(type(num2), num2)