# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-17 2:44 PM
class UserInfo(object):

    def __init__(self, name, age, account):
        self.name = name
        self._age = age
        self.__account = account

    def get_account(self):
        return self.__account


class UserInfo2(UserInfo):
    pass


if __name__ == '__main__':
    userInfo2 = UserInfo2('zhangsan', 18, 10086);
    print(userInfo2.get_account())
