# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-19 2:02 PM
from enum import Enum, unique

Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# @unique 装饰器可以帮助我们检查 保证没有重复值
@unique
class Month(Enum):
    Jan = 'January'
    Feb = 'February'
    Mar = 'March'
    Apr = 'April'
    May = 'May'
    Jun = 'June'
    Jul = 'July'
    Aug = 'Auguster'
    Sep = 'September'
    Oct = 'October'
    Nov = 'November'
    Dec = 'December'

if __name__ == '__main__':
    print(Month.Jan, '----', Month.Jan.name, '----', Month.Jan.value)
    for name, member in Month.__members__.items():
        print(name, '------', member, '------', member.value)