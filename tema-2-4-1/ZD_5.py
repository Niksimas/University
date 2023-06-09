"""
Создайте функцию whatPower2(x), которая принимает целое число и возвращает, какой степенью двойки оно является. Вернуть -1, если не является степенью двойки.
"""



def whatPower2(x):
    z = 0
    while 2**z <= x:
        if x == 2**z:
            return z
        z += 1
    return -1

ts = [1, 2, 4, 8, 16, 32, 10, 20, 30, 40]
for x in ts:
    print(x, whatPower2(x))
