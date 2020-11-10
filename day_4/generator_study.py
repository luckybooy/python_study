# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-09 11:33 AM
list1 = [x*x for x in range(3)]
print(list1)

print("-----------dividing line----------")
#generator 生成器 最简单的方式就是将list 的中括号'[]'修改为:小括号'()'
generator1 = (x*x for x in range(3))

print(generator1)

#遍历生成器
for x in generator1:
    print(x)