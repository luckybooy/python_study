# -*- coding: utf-8 -*-
# FileName : list_stu.py 
# Author : xiaoran
# Date : 2021-03-20 23:29
product_list = [
    ("手机", 5000),
    ("手表", 2500),
    ("电脑", 12000),
    ("平板", 8000)
]
print(product_list[0])

salary = input("请输入您的工资：")
# isdigit() 方法用来判断 值的是不是数字
if salary.isdigit():
    salary = int(salary)

    # 遍历数组中的元素
    for item in product_list:
        print(item)

    print("__________________________________________")
    # 2.遍历数组带索引
    for index, item in enumerate(product_list):
        print(index, item)
