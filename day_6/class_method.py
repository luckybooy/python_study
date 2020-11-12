# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-12 2:14 PM
class class_method:
    var1 = "world"

    @classmethod
    # @calssmethod  意思是：声明下边的函数是类函数
    # 类方法想要使用类属性，参数列表中必须加上一个cls，
    # cls意思就是把这个类作为参数，传给自己，这样就能调用类中的属性
    def fun1(cls):
        print("hello ",cls.var1)

    @classmethod
    def fun2( cls, arg):
        print(cls.var1)
        print(arg)

#class_method.fun1()
class_method.fun2(12)