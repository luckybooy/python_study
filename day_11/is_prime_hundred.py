

from math import sqrt

list1 = []
# 2～100 之间的素数
for num in range(2, 100):

    temp = int(sqrt(num))
    is_prime = False

    for x in range(2, temp + 1):
        if num % x == 0:
            is_prime = True
    if is_prime and num != 1:
        print('', end='')
    else:
        # print(num, end=' ')
        list1.append(num)
print(list1)

"""

import math
li = []
for num in range(2, 100):
    is_prime = True
    for factor in range(2, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            is_prime = False
            break
    if is_prime:
        li.append(num)
        # print(num, end=' ')
print(li)

"""