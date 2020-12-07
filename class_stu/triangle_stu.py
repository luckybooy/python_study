# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-12-07 4:20 PM
from math import sqrt


class Triangle(object):
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    # 静态方法
    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and a + c > b and b + c > a

    def peimeter(self):
        return self._a + self._b + self._c

    def area(self):
        harf = self.peimeter() / 2
        return sqrt(harf * (harf - self._a) * (harf - self._b) * (harf - self._c))

def main():
    a, b, c = 3, 4, 5
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print("周长：", t.peimeter())

        print("面积：", t.area())
    else:
        print("无法构成三角形")
if __name__ == '__main__':
    main()