"""
Создайте логическую функцию isSymmetric5,
которая принимает пятизначное число и проверяет,
является ли оно симметричным. Гарантируется,
что в качестве аргумента всегда приходит именно 5-значное число.
"""


def isSymmetric5(x):
    x_l = [i for i in str(x)]
    if (x_l[0] == x_l[4]) and (x_l[1] == x_l[3]):
        return True
    else:
        return False


ts = [12345, 44444, 12321, 87678, 12345, 85633, 73467]
for x in ts:
    if isSymmetric5(x):
        print(x, "+")
    else:
        print(x, "-")
