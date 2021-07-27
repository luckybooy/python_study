# -*- coding: utf-8 -*-
# FileName : sprider_test.py 
# Author : xiaoran
# Date : 2021-07-27 10:19
import requests

# push test
r = requests.get('https://www.qiushibaike.com/text/')  # 打开网址，一般我们会设置 请求头，来更逼真的模拟浏览器，下文有介绍
print(r.text)

