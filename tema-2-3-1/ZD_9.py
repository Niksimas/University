"""
    Создайте логическую функцию isFullSquare,
    которая принимает в качестве аргумента целое неотрицательное число и проверяет,
    является ли оно полным квадратом (True - является и False - не является).
"""


def isFullSquare(x):
    if (x ** 0.5) % 1 == 0.0:
        return True
    else:
        return False


for i in range(26):
    print(i, 'YES' if isFullSquare(i) else 'NO')

print()
for i in range(26):
    print(i, isFullSquare(i))
