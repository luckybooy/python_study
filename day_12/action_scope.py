# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-12-03 2:24 PM
def foo():
    global a    # global 修饰a，表示这里的a来自与全局变量，通过此种定义方法，可以将全局变量的a在函数内部进行修改
    a = 50
    print("-----子函数-----")
    print(a)
    # print(c)  # NameError: name 'c' is not defined
    def bar():
        a = 999
        print(a)
    bar()
if __name__ == '__main__':
    a = 100
    # print(b)  # NameError: name 'b' is not defined
    foo()
    print('-----主函数-----')
    print(a)