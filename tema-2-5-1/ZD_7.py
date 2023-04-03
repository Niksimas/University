"""
Простое число - это число, которое делится только на 1 и на само себя.
Например, простыми числами являются 11, 23 и 101.
Создайте логическую функцию isPrime (возвращает True/False),
которая принимает целое неотрицательное число и проверяет, является ли оно простым.
"""


def isPrime(a):
    delit = []
    for i in range(1, a + 1):
        if a % i == 0:
            delit.append(i)
    if delit == [1, a]:
        return True
    else:
        return False


numbers = [2, 3, 5, 7, 11, 17, 4, 6, 8, 9, 10, 12, 100, 23, 29]

for x in numbers:
    if isPrime(x):
        print(x)
