# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-06 4:58 PM
"""
迭代器的学习(iterator)有两种迭代形式，一种个iter(),另外一个是next()
"""

#字符创建迭代器对象
str1 = 'xiaoran'
iter1 = iter(str1)

#列表创建迭代器对象
list1 = [1, 2, 3, 4]
iter2 = iter(list1)

#元组 创建迭代器对象
tuple1 = ('beijing', 'shanghai', 'guangzhou', 'shenzhen', 'hangzhou')
iter3 = iter(tuple1)


str_test = 'goudaner'
iter4 = iter(str_test)


#for 循环遍历迭代器对象
for a in iter1:
    print(a, end=' ')
print("\n---------------------------")


while True:
    try:
        f = next(iter4)
    except StopIteration:
        break
    print(f, end=' ')

