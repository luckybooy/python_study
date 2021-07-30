# -*- coding: utf-8 -*-
# FileName : read_file_name.py 
# Author : xiaoran
# Date : 2021-07-29 14:23
# Desc : 获取文件夹中的文件名，并将文件名输出到excel中


# coding=utf-8
import os
import xlwt  # 操作excel模块
import sys

file_path = sys.path[0] + '/test.xls'  # sys.path[0]为要获取当前路径，test为要写入的文件
f = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 新建一个excel
sheet_desc = f.add_sheet('bug_name')  # 新建一个sheet

direct_dir = '/Users/ranchuangyun/Documents/yaxin/projects/大数据中台/漏洞修复/安全通报第五十七期到第七十期'
# pathDir = os.listdir(sys.path[0])  # 文件放置在当前文件夹中，用来获取当前文件夹内所有文件目录
pathDir = os.listdir(direct_dir)  # 文件放置在当前文件夹中，用来获取当前文件夹内所有文件目录

# print("pathDir is ", pathDir)
i = 0  # 将文件列表写入test.xls
for s in pathDir:
    sheet_desc.write(i, 0, s)  # 参数i,0,s分别代表行，列，写入值
    i = i + 1

f.save(file_path)


