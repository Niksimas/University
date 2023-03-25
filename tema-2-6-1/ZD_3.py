"""
   Создайте логическую функцию hasNextEqual(s),
   которая принимает в качестве аргумента строку и проверяет,
   есть ли в ней два подряд идущих одинаковых символа (True - есть, False - нет).
"""


def hasNextEqual(s):
    for i in range(len(s)):
        if (s[i-1] == s[i]) and len(s) > 1:
            return True
    return False


ts = ['Apple', '123455678', 'Dog', 'Spring']
for s in ts:
    print(s, '+' if hasNextEqual(s) else '-')
