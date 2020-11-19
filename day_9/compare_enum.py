# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-19 2:33 PM

from enum import Enum
class User(Enum):
    xiaoming = 18
    goudaner = 25
    Tom = 23

xiaoming = User.xiaoming
goudaner = User.goudaner

print(xiaoming == goudaner, xiaoming == User.xiaoming)
print(xiaoming is goudaner, xiaoming is User.xiaoming)

try:
    print('\n'.join(' ' + s.name for s in  sorted(User)))
except TypeError as err:
    print(' Error:{}'.format(err))