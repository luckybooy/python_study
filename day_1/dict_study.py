# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-04 3:40 PM
"""
dict 是key-value 用花括号包括
"""

animals = { '1001': 'tiger', '1002': 'lion'}
print(animals['1001'])
animals['1003'] = 'panda'   #添加一个字典值

print(animals)
dongwu = animals.copy()     #复制一个字典
print(dongwu)
dongwu.clear()      #清空字典
print(dongwu)
animals.pop('1001') #删除字典值
print(animals)

animals['1004'] = 'monkey'

print(animals.get('1002'))  #获取字典中的某个对应值
print(animals)

#print(animals.popitem())    #随机返回一个字典的key-value，并删除一个键值对

print(len(animals))
print(animals.items())
print('返回字典的key值:')
print(animals.keys())
print('返回字典的value值:')
print(animals.values())