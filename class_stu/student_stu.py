# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-12-04 2:02 PM
class Student(object):
    # __init__()是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法可以将学生对象对name和age两个属性进行绑定
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    # 定义了一个看电影的方法
    def watch_movie(self):
        if self.age < 18:
            print('%s只能看《奥特曼》' % self.name)
        else:
            print('%s正在看美国大片' % self.name)


def main():
    '''
    创建一个学生对象
    '''
    stu1 = Student('lihua', 18)
    stu1.study('English')
    stu1.watch_movie()

if __name__ == '__main__':
    main()