# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-12-15 3:38 PM
def nonlocal_test():
    count = 0

    def test2():
        nonlocal count
        count += 1
        return count

    return test2

val = nonlocal_test()
print(val())
print(val())
print(val())