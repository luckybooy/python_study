# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-17 3:35 PM
class User(object):
    def __init__(self, name):
        self.name = name

    def printUser(self):
        print('Hello!' + self.name)

class UserVip(User):
    def printUser(self):
        print('Hello!尊敬的Vip用户：'+self.name)

class UserGeneral(User):
    def printUser(self):
        print('Hello!尊敬的用户：'+ self.name)


def printUserInfo(user):
    user.printUser()



if __name__ == '__main__':
    userVip = UserVip('xiaoran')
    printUserInfo(userVip)

    userGeneral = UserGeneral('lincong')
    printUserInfo(userGeneral)

    # 输出结果
    # Hello!尊敬的Vip用户：xiaoran
    # Hello!尊敬的用户：lincong