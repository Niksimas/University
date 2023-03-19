"""Создайте процедуру printDecompositionV2,
которая принимает в качестве аргумента целое число и выводит его разложение на простые множители
с указанием степеней (см. примеры)."""


def printDecomposition(x):
    num = {}
    if x == 2:
        print(2)
        return
    while x > 1:
        for i in range(2, x+1):
            if x % i == 0:
                x //= i
                try:
                    num[i] += 1
                except KeyError:
                    num[i] = 1
                break
    result = ""
    for i in num:
        if num[i] == 1:
            result += f"{i}"
        else:
            result += f"{i}^{num[i]}"
        result += " * "
    print(result[:-2])


ts = [2, 6, 24, 30, 60, 500, 121, 1000, 999000]
for x in ts:
    print(x, '= ', end='')
    printDecomposition(x)
