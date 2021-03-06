
# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-20 11:20 AM
import threading
import time


class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print('thread,{}, @number,{}'.format(self.name, i))
            time.sleep(1)


def main():
    print("Start main threading")

    # 创建三个线程
    threads = [MyThread() for i in range(3)]

    #启动三个线程
    for t in threads:
        t.start()

    """合并线程
    """
    for t in threads:
        t.join()

    print("End main threading")

if __name__ == '__main__':
    main()