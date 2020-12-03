import math

"""
# 斐波那契数列
a = 0
b = 1
for i in range(1, 20):
    a, b = b, a + b
    print(b, end=' ')

print()

# 1~100之间的素数
list1 = []
is_prime = True
for num in range(1, 100):
    for x in range(2, int(math.sqrt(num)) + 1):
        if num % x == 0:
            is_prime = False
            break
    if is_prime and num != 1:
        list1.append(num)
print(list1)


list2 = []
for num in range(1, 100):
    temp = int(math.sqrt(num))
    is_prime = False
    for factor in range(2, temp + 1):
        if num % factor == 0:
            is_prime = True
            break
    if is_prime and num != 1:
        print('', end='')
    else:
        list2.append(num)
print(list2)



# 1～10000完美数 :出本身外其他素有因子之和等于该数本身的数字就是完美数字

for num in range(1, 10000):
    result = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            result += factor
            if factor > 1 and num // factor != factor:
                result += num // factor
    if num == result:
        print(result, end=' ')
"""
"""
# num = int(input('正整数:'))
# reversed_num = 0

for num in range(100, 1000):

    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if low ** 3 + mid ** 3 + high ** 3 == num:
        print(num)

print(low, mid, high)
"""

"""
# 数字反转
while True:
    num = int(input("输入一个数："))
    reversed_num = 0
    if num == 99999:
        break
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    print(reversed_num)

"""

"""
num = int(input('正整数 = '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)
"""

# 斐波那契数列
'''
a = 0
b = 1
for i in range(1, 20):
    a, b = b, a + b
    print(b, end=' ')
'''

"""
# 素数

list_num = []
for num in range(1, 100):
    mid = int(math.sqrt(num))
    is_prime = True
    for i in range(2, mid + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime and num != 1:
        list_num.append(num)
    else:
        print('', end='')
print(list_num)
"""
import os
import shutil

source_path = os.path.abspath(r'/Users/xiaoranya/Documents/work/company/project/小短案件11-23/1127====/案件资料--1127/公用的')
target_path = os.path.abspath(r'/Users/xiaoranya/Desktop/test')
for root, dirs, files in os.walk("/Users/xiaoranya/Desktop/test", topdown=False):
    for name in dirs:
        name_1 = os.path.join(root, name)
        # print(name_1)
