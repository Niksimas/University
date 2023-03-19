"""
    Создайте логическую функцию isSymmetric,
    которая принимает в качестве аргумента произвольное целое неотрицательное число и проверяет,
    имеет ли оно симметричную запись, например, подобно числам 121, 3333 или 1234321.
"""


def isSymmetric(x):
    if x < 10:
        return True
    x_l = [int(i) for i in str(x)]
    x_n = len(x_l) - 1
    for i in range(len(x_l) // 2):
        if x_l[i] != x_l[x_n]:
            return False
        x_n -= 1
    return True


ts1 = [123321, 1234567890987654321, 555555555555555, 11, 121, 12345, 100100, 23, 6, 0, 31]
print("Symmetric:")
for x in ts1:
    if isSymmetric(x):
        print(x)

ts2 = [234, 43, 112233445566, 432, 565, 556655, 87654, 45454, 3334, 23]
print()
print("Not symmetric:")
for x in ts2:
    if not isSymmetric(x):
        print(x)

print()
for x in ts1:
    print(x, isSymmetric(x))
