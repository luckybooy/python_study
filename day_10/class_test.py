# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-20 10:32 AM

def printHello(self, name = 'Py'):
    # 定义一个打印hello的函数
    print('Hello,', name)

# 动态创建一个Hello 类
Hello = type('Hello', (object,), dict(hello=printHello))
# 实例化Hello类
h = Hello()
# 调用Hello类的方法
h.hello()
# 查看Hello class 类的类型
print(type(Hello))
# 查看实例化 h 类的类型
print(type(h))

