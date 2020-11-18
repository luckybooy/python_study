# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-18 11:02 AM
class Number(object):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        print("__eq__")
        return self.value == other.value

    def __ne__(self, other):
        print("__ne__")
        return self.value != other.value

    def __lt__(self, other):
        print("__lt__")
        return self.value < other.value

    def __gt__(self, other):
        print("__gt__")
        return self.value > other.value

    def __le__(self, other):
        print("__le__")
        return self.value <= other.value

    def __ge__(self, other):
        print("__ge__")
        return self.value >= other.value

if __name__ == '__main__':
    num1 = Number(2)
    num2 = Number(3)
    print('num1 == num2 ?------> {} \n'.format(num1 == num2))
    print('num1 != num2 ?------> {} \n'.format(num1 != num2))
    print('num1 > num2 ?------> {} \n'.format(num1 > num2))
    print('num1 < num2 ?------> {} \n'.format(num1 < num2))
    print('num1 >= num2 ?------> {} \n'.format(num1 >= num2))
    print('num1 <= num2 ?------> {} \n'.format(num1 <= num2))
