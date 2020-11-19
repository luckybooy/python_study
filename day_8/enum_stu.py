# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-18 11:34 AM

# 枚举学习
from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# 遍历枚举类型
for name, member in Month.__members__.items():
    print(name, '------>', member, '------>', member.value)

print('\n', Month.Jan)
print(Month.__members__.items())