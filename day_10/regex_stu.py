# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-20 1:56 PM

# 自定义一个变量
import re

aa = 'iphone, xiaomi, huawei, meizu, samsung'
print('字符串中是否包含："xiaomi" 这个字符串:{}'.format((aa.index('xiaomi'))))
print('字符串中是否包含："xiaomi" 这个字符串:{}'.format((aa.index('xiaomi'))> -1))

print('字符串中是否包含："meizu" 这个字符串:{}'.format('meizu' in aa))

bb = "xiao ming is a good boy"
# 正则
findall = re.findall('gooda', bb)
print(findall)

if len(findall) > 0:
    print("定义的变量中包含目标字符串")
else:
    print("不包含，毛都没找到。")

# 正则找大写字母
cc = "Welcome to HenNan ZhengZhou..."
findall2 = re.findall('[A-Z]', cc)
print(findall2)