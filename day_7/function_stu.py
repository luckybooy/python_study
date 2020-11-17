# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-17 2:25 PM
class Fun_stu(object):

    #__init__(self) 函数就是初始化函数，也叫构造函数， 固定写法
    def __init__(self,str):
        print("实例化话成功")
        print("第二个参数是{}".format(str))


    #销毁对象
    def __del__(self):
        print("实例被销毁了。")
A = Fun_stu("xiaoming")
del(A)
