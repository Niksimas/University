"""
    Создайте логическую функцию isHappyNumber,
    которая принимает в качестве аргумента произвольное число и проверяет,
    является ли оно счастливым. Будем называть число счастливым,
    если произведение его цифр равно их сумме,
    например, 312. 3+1+2 = 3*1*2 = 6.
"""

import math


def isHappyNumber(x):
    x = [int(i) for i in str(x)]
    if sum(x) == math.prod(x):
        return True
    else:
        return False


ts = [123, 1142, 11331, 11512, 765, 234567, 234234, 621111]
for x in ts:
    if isHappyNumber(x):
        print(x, "+")
    else:
        print(x, "-")
