"""
Создайте функцию gcd (greatest common divisor),
которая принимает в качестве аргументов два натуральных числа
и возвращает их наибольший общий делитель.
"""


def scm(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)



numbers = [20, 30, 24, 99, 120]

for x in numbers:
    for y in numbers:
        if x<=y:
            print('scm(%d, %d) = %d' % (x, y, scm(x,y)))

