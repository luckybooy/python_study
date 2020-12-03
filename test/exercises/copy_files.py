# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-12-03 10:21 AM
import os
import shutil

source_path = os.path.abspath(r'/Users/xiaoranya/Documents/work/company/project/小短案件11-23/1127====/案件资料--1127/公用的')
# target_path = os.path.abspath(r'/Users/xiaoranya/Desktop/test')
for root, dirs, files in os.walk("/Users/xiaoranya/Desktop/test", topdown=True):
    for name in dirs:
        target_path_1 = os.path.join(root, name)

    if not os.path.exists(target_path_1):
        os.makedirs(target_path_1)
        if os.path.exists(source_path):
            # root 所指的是当前正在遍历的这个文件夹的本身的地址
            # dirs 是一个 list，内容是该文件夹中所有的目录的名字(不包括子目录)
            # files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)
            for root, dirs, files in os.walk(source_path):
                for file in files:
                    src_file = os.path.join(root, file)
                    shutil.copy(src_file, target_path_1)
                    print(src_file)

        print('copy files finished!')