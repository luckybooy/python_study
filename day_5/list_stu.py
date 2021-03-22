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

print("红色数字 \033[31;1m%s\033[0m" %(123))
# \033[颜色对应的数字;1m 需要显色的内容 \033[0m 固定格式
print("\033[34;1m hello \033[0m")
