"""
    Инверсия числа a по модулю m – это такое число b, что остаток от деления числа a*b на число m равен 1.
    Создайте функцию inversion(a, m), которая принимает a и m, а возвращает инверсию a по модулю m.
    Инверсия существует только для взаимно простых a и m. Если инверсии не существует, то вернуть -1.
"""
from math import gcd


def inversion(x, c):
    if gcd(x, c) == 1:
        for i in range(c):
            if ((x * i) % c) == 1:
                return i
    return -1


m = 24
for a in range(10, 20):
    print('inversion(', a, ', ', m, ') = ', inversion(a, m), sep='')
print()

m = 23
for a in range(1, 10):
    print('inversion(', a, ', ', m, ') = ', inversion(a, m), sep='')
