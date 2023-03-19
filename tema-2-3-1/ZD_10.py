"""
Создайте логическую функцию isFullCube,
которая принимает в качестве аргумента целое неотрицательное число и проверяет,
является ли оно полным кубом (True - является и False - не является).
"""
import math


def isFullCube(x):
    if round(pow(x, 1/3), 0) ** 3 == x:
        return True
    else:
        return False


ts = [1, 8, 27, 64, 4, 9, 16, 25, 12, 24, 40]
for i in ts:
    print(i, 'YES' if isFullCube(i) else 'NO')

tz = [100, 1728, 144, 1000, 999, 64000, 625]
for x in tz:
    print(x, 'YES' if isFullCube(x) else 'NO')