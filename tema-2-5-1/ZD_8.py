"""
Создайте процедуру printPrimes, которая принимает в качестве аргумента целое число
и выводит все простые числа, не превосходящие этого числа.
Выводить следует через запятую с пробелом, а в конце поставить точку.
"""


def printPrimes(a):
    print(2, end="")
    for i in range(3, a + 1):
        delit = []
        for j in range(1, i+1):
            if i % j == 0:
                delit.append(j)
        if delit == [1, i]:
            print(f", {i}", end="")
        del delit
    print(".")


numbers = [2, 3, 7, 24, 17, 30]

for x in numbers:
    print(x, end=": ")
    printPrimes(x)

