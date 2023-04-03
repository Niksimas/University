"""
    Создайте процедуру printPowers(x,y),
    которая принимает два целых числа и выводит все степени числа y,
    не превосходящие числа x. После окончания вывода перевести курсор на новую строку.
"""


def printPowers(x, y):
    z = 0
    while y**z<x:
        print(y**z, end=" ")
        z += 1
    print()


printPowers(100, 2)
printPowers(1000, 3)
printPowers(10000, 5)
