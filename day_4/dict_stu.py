# -*- coding: utf-8 -*-
# FileName : dict_stu.py 
# Author : xiaoran
# Date : 2021-03-22 21:28
# 字典学习

info = {}
print(info)
# 新增元素
info[1001] = "张三"
info[1002] = "李四"
info[1003] = "马六"
# 多个元素之间用逗号分开
print(info)
info[1001] = "zhangsan"
print(info)
# 查
print(info[1003])

# 删除1001对应的元素
info.pop(1001)
print(info) # 推荐使用 的删除方法
# 10010 有则修改，无则删除
info[10010] = "习大大"

del info[10010]
print(info)