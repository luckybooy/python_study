# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-12 2:39 PM

"""
修改类的属性值
"""
class modify_ages:
    arg1 = "cup"
    arg2 = "car"


    # 从内部开始新增和修改函数的属性值
    @classmethod
    def test_modify(cls):
        print("初始参数值为：{}".format(cls.arg1))
        arg1_after = input("Please input new value:")
        print("修改后的值为：{}".format(arg1_after))

        # 新增一个参数
        cls.arg3 = input("Please input new arg:")

        print(("新增的参数为：{}".format(cls.arg3)))

        print(cls.arg3)


modify_ages.test_modify()

modify_ages.arg1 = input("Please input a new value for arg1:")
print("我那个外部修改后的arg1值为：{}".format(modify_ages.arg1))

modify_ages.arg5 = input("Please add a arg:")
print("新增的arg5的参数值为：{}".format(modify_ages.arg5))

