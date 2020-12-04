# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-12-03 4:53 PM
def get_suffix(filename, has_dot=False):
    """
    获取文件的后缀名
    :param filename: 文件名
    :param has_dot: 返回的后缀名需要带点
    :return:文件的后缀名
    """

    pos = filename.rfind('.')
    print(pos, len(filename))
    
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        #print(filename[index:])
        return filename[index:]

    else:
        return ''

get_suffix('action_scope.py', has_dot=False)