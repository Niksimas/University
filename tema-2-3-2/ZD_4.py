"""
Создайте логическую функцию isDifferent,
которая принимает в качестве аргумента целое число
и проверяет все ли его цифры различны
True - все различны, False - есть повторения).
"""


def isDifferent(x):
    x_l = [int(i) for i in str(x)]
    for i in range(len(x_l)):
        for j in range(len(x_l)):
            if (i != j) and (x_l[i] == x_l[j]):
                return False
    return True


ts = [11, 131, 70256, 334, 5432345, 76547, 8642]
for x in ts:
    print(x, 'YES' if isDifferent(x) else 'NO')
