# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-12-03 11:23 AM

import os
import shutil

def copy_allfiles(src,dest):
#src:原文件夹；dest:目标文件夹
  src_files = os.listdir(src)
  for file_name in src_files:
    full_file_name = os.path.join(src, file_name)
    if os.path.isfile(full_file_name):
        shutil.copy(full_file_name, dest)

src_path = "/Users/xiaoranya/Documents/work/company/project/小短案件11-23/1127====/案件资料--1127/公用的"
tar_path = "/Users/xiaoranya/Documents/work/company/project/小短案件11-23/1127====/案件资料--1127"
for root, dirs, files in os.walk(tar_path, topdown=False):
    for name in dirs:
        target_path = os.path.join(root, name)
        copy_allfiles(src_path, target_path)

    #copy_allfiles(src_path, target_path)