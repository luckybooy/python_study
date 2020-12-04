# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-12-04 2:16 PM

"""
在python中访问权限也有公开的和私有的
如果想要属性是私有的，在给属性命名的时候就用两个下划线开头 eg: __foo 、__bar(self)
"""
class Test:
    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')

def main():
    test = Test('Hello')
    # AttributeError: 'Test' object has no attribute '__bar'
    test.__bar()
    #print(test.__foo)   #AttributeError: 'Test' object has no attribute '__foo'

if __name__ == '__main__':
    main()