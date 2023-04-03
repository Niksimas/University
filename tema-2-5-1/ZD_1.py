"""
    Создайте процедуру printDivision(a,b),
    которая выполняет деление с остатком числа a на b и выводит результат (см. примеры).
"""


def printDivision(x, y):
    print(f"{x} = {x // y} * {y} + {x % y}")


for i in range(3, 13):
    printDivision(24, i)
