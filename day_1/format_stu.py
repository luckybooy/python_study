# -*- coding: utf-8 -*-
# FileName : format_stu.py 
# Author : xiaoran
# Date : 2021-03-14 01:12
name = "xiaoran"
name2 = name
print(name, name2)
name = "goudaner"
print(name, name2)

name = input("Name:")
age = input("Age:")
job = input("Job")
salary = input("Salary")

info = """
====================info of %s====================
name:%s
age:%s
job:%s
salary:%s
====================info of ========================
""" % (name, name, age, job, salary)
print(info)

info2 = """
====================info of {0}====================
name:{0}
age:{1}
job:{2}
salary:{3}
====================info of ========================
""".format(name, age, job, salary)
print(info2)
