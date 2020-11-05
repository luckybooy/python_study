# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-04 4:21 PM
"""
set 集合 的学习
特点：无序，值唯一
python 中集合的定义格式：集合名称 = set ([])
"""
set1 = set([1, 2, 3, 4, 5, 6, 6, 6])
print(set1)
#添加元素
set1.add(7)
print(set1)
#删除元素
set1.remove(6)
print(set1)

set2 = set('hello')
print("set2的集合:", set2)
set3 = set(['p', 'y', 't', 'h', 'o', 'n'])
print("set3的集合:", set3)
#两个集合的交集 '&'
print(set2 & set3)
#两个集合的并集 '|'
print(set2 | set3)
#差集 '-'
print("set2和set3的差集是：", set2 - set3)

print("set3和set2的差集是：", set3 - set2)