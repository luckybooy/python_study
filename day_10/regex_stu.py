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

# '\d' 表示 匹配所有数字字符的规则 其目的是和'[0-9]' 表达的意思是一样的
dd = '12, xiaoming, 23, 狗蛋儿, 45, heihei, 88'
findall3 = re.findall('\d', dd)
print(findall3)

findall4 = re.findall('[0-9]', dd)
print(findall4)

ee = '"12san", san21, 45liu,qi89'
ff = 'xiaoming, 22, gou, 66, qiqi'
findall5 = re.findall('\A' ,ff)
print(findall5)