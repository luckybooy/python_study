# -*- coding: utf-8 -*-
# FileName : guess_num.py 
# Author : xiaoran
# Date : 2021-03-15 23:07
lucky_num = 27
guess_nun = int(input("guess number:"))

if guess_nun == lucky_num:
    print("Wow,You are great!")
elif guess_nun > lucky_num:
    print("guess bigger...")
else:
    print("guess smaller...")
