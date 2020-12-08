# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-12-08 10:58 AM
class Person(object):
    """人"""

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        print('%s正在愉快的玩耍。' % self._name)

    def watch_tv(self):
        if self._age >= 18:
            print('%s正在看美国大片。' % self._name)
        else:
            print('%s正在看动画片。' % self._name)

class Student(Person):
    """学生"""

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s的%s正在学习%s。' % (self._grade, self._name, course))

class Teacher(Person):
    """老师"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def touch(self, course):
        print('%s%s正在讲%s。' % (self._name, self._title, course))

def main():
    stu = Student('xiaoran', 22, '大三')
    stu.study('English')
    stu.watch_tv()
    print('-------------dividing line-------------')
    t = Teacher('岳岳', 26, '班主任')
    t.watch_tv()
    t.play()
    t.touch('语文')

if __name__ == '__main__':
    main()