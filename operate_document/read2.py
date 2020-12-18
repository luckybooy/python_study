# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-12-18 5:38 PM
import time

"""
读取文件的三种方式
"""


def main():
    # 一次性读取整个文件内容
    with open('read_docu_test.py', 'r', encoding='utf-8') as f:
        print(f.read())

    # 通过for-in 循环逐行读取
    with open('read_docu_test.py', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    # 读取文件按行读取到列表中
    with open('read_docu_test.py') as f:
        lines = f.readlines()
    print(lines)


if __name__ == '__main__':
    main()



