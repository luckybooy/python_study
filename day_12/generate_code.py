# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-12-03 4:44 PM
import random

def generate_code(code_len = 4):
    """
    生成指定长度的验证码
    :param code_len: 验证码长度(默认设置为4个字符)
    :return:由大小写和数字构成的验证码
    """

    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    print(code)

generate_code(4)
