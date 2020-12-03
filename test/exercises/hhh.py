# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-23 1:47 PM

t = ('骆昊', 38, True, '四川成都')
print(t)
# 获取元组中的元素
print(t[0])
print(t[3])
# 遍历元组中的值
for member in t:
    print(member)

t = ('王大锤', 20, True, '云南昆明')
print(t)
# 将元组转换成列表
person = list(t)
print(person)
person[0] = '李小龙'
person[1] = 25
print(person)

fruits_list = ['apple', 'banana', 'orange']
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)

set1 = {1, 2, 3, 4, 5, 5}
print(set1)
print(len(set1))

set2 = set(range(1, 10))
set3 = set((1, 2, 3, 4, 5, 5))
print(set2, set3)
set4 = {x for x in range(1, 100) if x % 3 == 0 or x % 5 == 0}
print('set4 = {}'.format(set4))

set1.add(77)
set1.add(88)
set2.update([11, 12])
print(set2)
set2.discard(5)
if 4 in set2:
    set2.remove(4)
print(set1, set2)
print(set3.pop())
print(set3)