# -*- coding: utf-8 -*-
# FileName : shuju_ste.py 
# Author : xiaoran
# Date : 2021-03-18 23:10
import copy

names = ['张三', '李四', '王武', '马六', '钱七']
print(names)

print(names[1:3])

print(names[1])
# -1 选择最后一个元素
print(names[-1])
# 取最后两个
print(names[-2:])
# 取下标为2及以后的元素
print(names[2:])
# 追加
names.append('王强')
print(names)

# 在下标为1的位置插入
names.insert(1, "秦叔宝")
print(names)

# 替换 脚标位置的元素
names[2] = 'lisi'
print(names)

names.pop(2)
print(names)

# 根据元素定位 在数组中的位置
index = names.index('钱七')
print(index)

names.append("张三")
print(names)

# 统计数量
counts = names.count("张三")
print(counts)

print('*********************************************************************')
names2 = copy.copy(names)
print(names2)
names[1] = '张思'
print(names)
print("……………………………………………………………………")
print(names2)
