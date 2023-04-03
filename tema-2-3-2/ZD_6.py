"""
Создайте логическую функцию isFib,
которая принимает в качестве аргумента целое неотрицательное число и проверяет,
является ли оно числом Фибоначчи (True - является и False - не является).
"""


def isFib(x):
    fib_num = [0, 1, 1]
    for i in range(2, x + 1):
        fib_num.append(fib_num[i - 1] + fib_num[i])
    if x in fib_num:
        return True
    else:
        return False


for i in range(36):
    print(i, 'YES' if isFib(i) else 'NO')