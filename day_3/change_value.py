# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-06 2:38 PM
"""
def change_number(a):
    a = 666

a = 1
change_number(a)
print(a)


def change_value(b):
    print("进入函数体。。。")
    print('函数一开始b的值:{}'.format(b))
    b = 1000
    print('函数中b赋值后的值：{}'.format(b))

b=2
change_value(b)
print('最后输出b的值：{}'.format(b))
"""

"""
#当参数是可变类型时，其输入结果也会改变 （可改变类型有：list，set，dict）
def change_list(a):
    print("函数一开始的值为：{}".format(a))
    a.append(666)
    print("变更后的值为：{}".format(a))
    return ;

a = [11,22,44,33]
change_list(a)
print("最终值为：{}".format(a))

#错误事例 tuple 元组只要被初始化后,其里边的元素就不可改变
def change_tuple(a):
    print("初始值为：{}".format(a))
    print(a[2])
    # a[2] = 'haha'
    a = ('haha',)
    print("变更后的值为：{}".format(a))
    return ;

a = ('hello', 'hi', 'love', 'heihei')
change_tuple(a)
print("最终值为:{}".format(a))
"""

'''
set 集合无序，唯一'''


def change_set(a):
    print("初始值为：{}".format(a))
    a.add('xiaopeng')
    print("变更后的值为：{}".format(a))
    return


a = set(['xiaohua', 'xiaohong', 'lidan'])
change_set(a)
print("最终值为:{}".format(a))
