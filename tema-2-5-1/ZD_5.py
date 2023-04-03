"""
Создайте функцию gcd (greatest common divisor),
которая принимает в качестве аргументов два натуральных числа
и возвращает их наибольший общий делитель.
"""


def gcd(a, b):
    a_del = []
    b_del = []
    for i in range(1, a + 1):
        if a % i == 0:
            a_del.append(i)
    for i in range(1, b + 1):
        if b % i == 0:
            b_del.append(i)
    cd = list(set(a_del) & set(b_del))
    return max(cd)



numbers = [2, 3, 4, 9, 12, 15, 24]

for x in numbers:
    for y in numbers:
        if x <= y:
            print('gcd(%d, %d) = %d' % (x, y, gcd(x, y)))
