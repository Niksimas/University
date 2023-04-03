"""
Создайте функцию stringSum, которая принимает в качестве аргумента строку,
в которой записаны целые числа через ровно один пробел, и возвращает сумму этих чисел.
"""
from math import gcd


def stringSum(a):
    num = [int(i) for i in a.split(" ")]
    return sum(num)


strings = [
    "13 43 65 0 0 87 9 9 56789",
    "100",
    "1 2 3",
    "5123123123 2323 99987",
    "0 0 0"
    ]

for s in strings:
    print(stringSum(s))