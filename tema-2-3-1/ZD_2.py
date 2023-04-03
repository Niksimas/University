"""
    Создайте логическую функцию isDigits4, которая принимает в качестве аргумента целое число
    и проверяет, является ли оно 4-значным (True - является и False - иначе).
"""


def isDigits4(x):
    if len(str(x)) == 4:
        return True
    else:
        return False


ts = [12, 34, 56, 123, 345, 456, 2345, 6543, 7654, 8765, 1234567, 2345678]
for i in ts:
    print(i, 'YES' if isDigits4(i) else 'NO')
