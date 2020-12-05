# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-12-04 5:34 PM
class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器get 方法
    @property
    def name(self):
        return self._name

    # 访问器get 方法
    @property
    def age(self):
        return self._age

    # 修改器 set 方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age < 18:
            print('%s正在玩过家家...' % self._name)
        else:
            print('%s正在玩斗地主...' % self._name)

def main():
    person = Person('林冲', 27)
    person.play()
    print("------- dividing line -------")
    person.age = 16
    person.play()


if __name__ == '__main__':
    main()

