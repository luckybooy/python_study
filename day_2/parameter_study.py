# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-05 6:18 PM


def print_user_info(name, age, sex='男',hobby='basketball'):    #只有在形参表末尾的参数才能设置默认值
    print("昵称：{}".format(name),  end=',')
    print("年龄：{}岁".format(age), end=',')
    print("性别:{}".format(sex), end=',')
    print("爱好：{}".format(hobby))
    return


print_user_info('xiaoming', 18, 'man')
print_user_info('萧然', 22)

#不定长参数
def print_user_info(name, age, address, *friends, gender = '男'):
    print("姓名：{}".format(name), end=',')
    print("年龄：{}".format(age), end=',')
    print("地址：{}".format(address), end=',')
    print("性别：{}".format(gender), end=',')
    print("朋友：{}".format(friends))


#print_user_info('小明', 18, '北京', 'man', '小红', '小花', '小青')
print_user_info('小明', 18, '北京', '小红', '小花', '小青')