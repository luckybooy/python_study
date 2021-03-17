# -*- coding: utf-8 -*-
# FileName : decode_test.py 
# Author : xiaoran
# Date : 2021-03-17 23:48
str = "萧燃真帅"
print(str)
print("utf-8的编码格式为：", str.encode('utf-8'))

print('===================================')
print(str.encode('utf-8').decode('utf-8'))
