"""
Создайте логическую функцию isHappyNumber,
которая принимает в качестве аргумента 3-значное число и проверяет,
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


ts = [123, 654, 876, 312]
for x in ts:
    if isHappyNumber(x):
        print(x, "+")
    else:
        print(x, "-")
