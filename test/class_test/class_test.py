# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-12-08 1:49 PM
class ObjectCreator(object):
    pass

my_class = ObjectCreator()
print(my_class)

def choose_class(name):
    if name == 'Foo':
        class Foo(object):
            pass
        return Foo
    else:
        class Bar(object):
            pass
        return Bar

MyClass = choose_class('Foo')
print(MyClass)  # 返回类 <class '__main__.choose_class.<locals>.Foo'>
print(MyClass()) # 可以通过这个类创建类实例，也就是对象   <__main__.choose_class.<locals>.Foo object at 0x7f933d1fd0a0>
