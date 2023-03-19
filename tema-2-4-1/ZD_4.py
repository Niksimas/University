"""
Создайте логическую функцию isPower(x,y), которая принимает два целых числа и проверяет, является ли x степенью y (True - является и False - не является).
"""


def isPower(x, y):
    z = 0
    while y**z <= x:
        if x == y**z:
            return True
        z += 1
    return False


ts = [4, 16, 27, 32, 64, 30, 40, 81]
for x in ts:
    print(x, 2, 'YES' if isPower(x, 2) else 'NO')
    print(x, 3, 'YES' if isPower(x, 3) else 'NO')
    print(x, 4, 'YES' if isPower(x, 4) else 'NO')
