# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-04 11:50 AM
name = ['小明', '李华', '钱庆', '田珠']
print(name)
print("--------------------------------")
print(name[2])
print("--------------------------------")
name.append('马总')       #追加元素
print(name)
print("--------------------------------")
del name[2]     #删除索引处的元素
print(name)
print("--------------------------------")
print(name[-1])
name[3]='魏总'        #修改索引处元素值
print(name)


print(len([1, 2, 3, 4]))

print(len(name))

print(['Hi'] * 4)
