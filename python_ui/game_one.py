# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-12-15 10:43 AM
import pygame

"""
def main():
    # 初始化导入的pygame中的模块
    pygame.init()
    # 初始化用于显示窗口并设置窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    # 设置当前窗口的标题
    pygame.display.set_caption('打球吃小球')
    # 设置窗口的背景色(颜色有红绿蓝三原色构成的元组)
    screen.fill((255, 255, 255))
    # 通过指定的文件名加载图像
    ball_image = pygame.image.load('./src/zuqiu.png')
    # 在窗口上渲染图像
    screen.blit(ball_image, (50, 50))
    #自己画的方式来展示图像
    # # 绘制一个圆(参数：屏幕, 颜色, 圆心位置, 半径, 0表示填充圆)
    # # pygame.draw.circle(screen, (255, 0, 0), (100, 100), 30, 0)
    # 刷新当前窗口(渲染窗口将绘制的图像呈现出来)
    pygame.display.flip()
    running = True
    # 开启一个事件循环处理发生的事件
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                running = False
"""

def main():
    # 初始化导入的pygame中的模块
    pygame.init()
    # 初始化用于显示的窗口并设置窗口的尺寸
    screen = pygame.display.set_mode((800, 600))
    # 设置当前窗口的标题
    pygame.display.set_caption('打球吃小球')
    # 定义变量来表示小球在屏幕上的位置
    x, y = 50, 50
    running = True
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (255, 0, 0,), (x, y), 30, 0)
        pygame.display.flip()
        # 每隔50毫秒就改变小球的位置再刷新窗口
        pygame.time.delay(50)
        x, y = x + 5, y + 5


if __name__ == '__main__':
    main()
