# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-23 1:47 PM

import random
def generate_code(code_len = 4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    print(all_chars[last_pos])
    print(last_pos)
    print('源长度为：%d' % len(all_chars))
    for i in range(0, len(all_chars)-1):
        print(i, end=' ')
    print("\n---------")
    code = ''
    for _ in range(code_len):
        code += all_chars[random.randint(0, last_pos)]
    print(code)

if __name__ == '__main__':
    generate_code()