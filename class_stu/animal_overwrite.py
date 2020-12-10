# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-12-08 11:21 AM

from abc import ABCMeta, abstractmethod

class Pet(object, metaclass=ABCMeta):
    """宠物"""

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        """发出声音"""
        pass

class Dog(Pet):
    """狗"""

    def make_voice(self):
        print('%s:汪汪汪...' % self._nickname)

class Cat(Pet):
    """猫"""
    def make_voice(self):
        print("%s:喵喵喵～～" % self._nickname)

def main():
    pets = [Dog('旺财'), Cat("加菲"), Dog('大黄'), Cat('凯蒂')]
    for pet in pets:
        pet.make_voice()

if __name__ == '__main__':
    main()