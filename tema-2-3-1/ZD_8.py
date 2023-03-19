"""
Создайте логическую функцию isLeap,
которая принимает в качестве аргумента год (целое число) и проверяет,
является ли он високосным (возвращает True для високосных и False - иначе).
"""


def isLeap(x):
    if (x % 4 == 0 and x % 100 != 0) or x % 400 == 0:
        return True
    else:
        return False


years = [2000, 1800, 1600, 2021, 1990, 1991, 1380, 1917, 1945, 1961]
for x in years:
    if isLeap(x):
        print(x)

print()
for x in years:
    print(x, isLeap(x))