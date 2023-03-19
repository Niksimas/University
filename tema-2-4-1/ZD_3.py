"""
    Создайте логическую функцию isPower2,
    которая принимает целое неотрицательное число и проверяет,
    является ли оно степенью двойки (True - является и False - не является).
"""


def isPower2(x):
    z = 0
    while 2**z <= x:
        if x == 2**z:
            return True
        z += 1
    return False


ts = [1, 2, 4, 8, 16, 32, 10, 20, 30, 40]
for x in ts:
    print(x, 'YES' if isPower2(x) else 'NO')
    
