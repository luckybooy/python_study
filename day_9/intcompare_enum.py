# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-19 4:18 PM
# int枚举 类型 排序
import enum
class User(enum.IntEnum):
    xiaoming = 26
    goudaner = 22
    lihua = 18

try:
    print('\n'.join(s.name for s in sorted(User)))
except TypeError as err:
    print( 'Err : {}'.format(err))