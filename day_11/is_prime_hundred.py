from math import sqrt
for num in range(2, 100):
    list = []
    temp = int(sqrt(num))
    is_prime = False

    for x in range(2, temp + 1):
        if num % x == 0:
            is_prime = True
    if is_prime and num != 1:
        print('', end='')
    else:
        print(num, end=' ')

