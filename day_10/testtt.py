# -*- coding: utf-8 -*-
# project_name: python_study
# author:xiaoran
# date:2020-11-23 10:56 AM
import random

"""
sum = 0
for i in range(101):
    sum += i
print(sum)

sum1 = 0
# 100 内的偶数求和
for j in range(2, 101, 2):
    sum1 += j
print(sum1)

sum2 = 0
# 50内的奇数求和
for g in range(1, 50, 2):
    print(g, end=' ')
    sum2 += g
print(sum2)


# rand = random.randint(1, 100)
rand = 66
Flag = True
count = 0
while Flag:
    count += 1
    guess = int(input("请猜一百以内的一个数："))
    if (guess > rand):
        print('大了')
    elif(guess == rand):
        print("Congratulation！！！")
        Flag = False
    else:
        print('小了')
    if(count > 2):
        print("猜的次数{}已达上限，game over".format(count))
        Flag = False

"""

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入: '))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('恭喜你猜对了!')
        break
print('你总共猜了%d次' % counter)
if counter > 7:
    print('你的智商余额明显不足')







