# -*- coding: utf-8 -*-
# FileName : sys_model_stu.py 
# Author : xiaoran
# Date : 2021-03-16 23:27
# Description:系统模块引用学习
import sys
import os


ool = os.path
print(ool)
# os.mkdir('test')      #创建文件夹
# os.rmdir('test')        #删除文件夹
oss = os.system('ls -l')
oss_22 = os.popen('ls').read()

print(oss)
print("===========================")
print(oss_22)

pwd = sys.path
pwd_all = sys.path_hooks
pathhh = sys.modules
print(pwd)
print(pwd_all)
print(pathhh)