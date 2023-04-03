"""
Создайте функцию whatPower(x,y), которая принимает два целых числа и возвращает, какой степенью y является x. Вернуть -1, если не является степенью y.
"""


def whatPower(x, y):
    z = 0
    while y**z <= x:
        if x == y**z:
            return z
        z += 1
    return -1


ts = [4, 16, 27, 32, 64, 30, 40, 81]
for x in ts:
    print(x, 2, '->', whatPower(x, 2))
    print(x, 3, '->', whatPower(x, 3))
    print(x, 4, '->', whatPower(x, 4))
