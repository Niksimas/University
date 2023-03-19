"""Создайте процедуру printDecomposition,
которая принимает в качестве аргумента целое число
и выводит его разложение на простые множители (см. примеры)."""


def printDecomposition(x):
    while x > 1:
        for i in range(2, x+1):
            if x % i == 0:
                x //= i
                print(i, end=" ")
                break
    print()


ts = [2, 6, 100, 1000, 999000]

for x in ts:
    printDecomposition(x)
