# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-17 3:24 PM

# 子类的类型判断

class User1(object):
    pass

class User2(User1):
    pass

class User3(User2):
    pass

if __name__ == '__main__':
    user1 = User1()
    user2 = User2()
    user3 = User3()

    # 可以通过isinstance() 就可以告诉我们，一个对象是否是某种类型
    print(isinstance(user3, User2))
    print(isinstance(user3, User1))
    print(isinstance(user3, User3))

    # 同时基本类型也能通过isinstance 来进行判断是否属于这种类型
    print(isinstance('xiaoran', str))
    print(isinstance(18, int))