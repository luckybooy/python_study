# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-10 5:20 PM
class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


for rr in reversed(Countdown(30)):
    print(rr, end=' ')

print()

print("----------dividing line----------")
for rr in Countdown(30):
    print(rr, end=' ')
print()