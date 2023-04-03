"""
Палиндром - это строка, которая одинаково читается слева-направо и справа-налево.
Создайте логическую функцию isPalindrom, которая принимает в качестве аргумента строку и проверяет,
 является ли она палиндромом (True - строка является палиндромом, False - не является).
"""


def isPalindrom(x):
    if len(x) < 2:
        return True
    x_l = [i for i in x]
    x_n = len(x_l) - 1
    for i in range(len(x_l) // 2):
        if x_l[i] != x_l[x_n]:
            return False
        x_n -= 1
    return True


words = ['apple', '123321', '121', 'qwertrew', '5']

for s in words:
    print(s, end=' - ')
    print('YES' if isPalindrom(s) else 'NO')
