"""
    Создайте функцию maxDivisor(a), которая принимает целое число и возвращает
    максимальный делитель этого числа отличный от него самого (см. примеры).
"""


def maxDivisor(x):
    for i in range(1, x):
        if x % i == 0:
            delit = i
    return delit


for i in range(10, 20):
    print('maxDivisor(', i, ') = ', maxDivisor(i), sep='')
    
