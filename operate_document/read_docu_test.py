# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-12-18 5:20 PM
def main():
    f = None
    try:
        f = open('__init__.py', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件夹')
    except LookupError:
        print('指定了未知的编码')
    except UnicodeDecodeError:
        print('读取文件时解码错误')
    finally:
        if f:
            f.close()


if __name__ == '__main__':
    main()
