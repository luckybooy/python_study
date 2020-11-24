# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-09 1:49 PM
def odd():
    print('step 1')
    yield (1)
    print('step 2')
    yield (2)
    print('step 3')
    yield (3)


o = odd()
print(next(o))
