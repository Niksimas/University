"""Создайте процедуру printCoprimes,
которая принимает в качестве аргумента целое число и выводит числа из диапазона от 1 до N,
которые взаимно просты с N. Вывод чисел должен быть через запятую с пробелом, а в конце - точка.
"""
from math import gcd


def printCoprimes(a):
    num = []
    for i in range(2, a):
        if gcd(a, i) == 1:
            num.append(i)
    print(num[0], end="")
    for i in range(1, len(num)):
        print(f", {num[i]}", end="")
    print(".")


ts = [3, 6, 11, 12, 24]
for x in ts:
    printCoprimes(x)