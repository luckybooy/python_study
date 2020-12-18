# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-12-18 5:20 PM
def main():
    f = open('__init__.py', 'r', encoding='utf-8')
    print(f.read())
    f.close()


if __name__ == '__main__':
    main()
