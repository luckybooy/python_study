# -*- coding: utf-8 -*-
# FileName : model_stu.py 
# Author : xiaoran
# Date : 2021-03-15 22:51

# 可以在控制台看效果
import getpass
"""
username = input("Username:")
passwd = getpass.getpass("Password:")

print(username, passwd)
"""

_username = 'xiaoran'
_password = '123456'
username = input("UserName:")
password = input("Password:")

if _username == username and _password == password:
    print("Welcome to {name} login...".format(name=username))
else:
    print("Invalid username or password!")