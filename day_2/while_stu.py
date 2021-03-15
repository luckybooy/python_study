# -*- coding: utf-8 -*-
# FileName : while_stu.py 
# Author : xiaoran
# Date : 2021-03-15 23:10
lucky_num = 24
guess_time = 0

while guess_time < 3:
    guess_num = int(input("guess a num:"))
    if guess_num == lucky_num:
        print("Great!")
        break
    elif guess_num > lucky_num:
        print("guess bigger...")

    else:
        print("guess smaller...")

    guess_time += 1

else:
    print("guess too many times,game over...")


