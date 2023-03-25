"""
Создайте логическую функцию hasRepeats,
которая принимает в качестве аргумента строку и проверяет,
есть ли в этой строке повторяющиеся символы
(True - есть повторы, False - нет повторов).
"""


def hasRepeats(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if (a[i] == a[j]) and len(a) > 1 and i != j:
                return True
    return False


strings = ['aplpe', 'abcde', '1111', '123456', '6', '77']

for s in strings:
    print(s, end=' - ')
    print('YES' if hasRepeats(s) else 'NO')