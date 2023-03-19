"""Функция Эйлера от числа N - это количество чисел из диапазона от 1 до N,
которые взаимно просты с N.

Создайте функцию euler, которая принимает в качестве аргумента целое число
и возвращает значение функции Эйлера от этого числа.

Создайте процедуру printCoprimes, которая принимает в качестве аргумента целое число
и выводит числа из диапазона от 1 до N, которые взаимно просты с N.
Вывод чисел должен быть через запятую с пробелом, а в конце - точка."""
from math import gcd


def printCoprimes(a):
    num = []
    for i in range(1, a):
        if gcd(a, i) == 1:
            num.append(i)
    print(num[0], end="")
    for i in range(1, len(num)):
        print(f", {num[i]}", end="")
    print(".")


def euler(a):
    num = []
    for i in range(1, a):
        if gcd(a, i) == 1:
            num.append(i)
    return len(num)


numbers = [12, 15, 11, 24]

for x in numbers:
    print("euler(%d) = %d" % (x, euler(x)))
    printCoprimes(x)
    print()