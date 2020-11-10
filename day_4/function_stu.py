# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-09 11:45 AM
def function_study():
    for i in range(9):
        print(i, end=' ')
    print()

function_study()
print("----------dividing line----------")
def fun_generator():
    for j in range(10):
        yield(j)

print(fun_generator())