"""
    Создайте логическую функцию isEven, которая принимает в качестве аргумента целое число и
    проверяет, является ли оно четным (True - четное составить и False - нечетное).
"""


def isEven(i):
    if i % 2 == 0:
        return True
    else:
        return False


for i in range(10):
    print(i, 'EVEN' if isEven(i) else 'ODD')
