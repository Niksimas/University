"""
    Создайте функцию longestString(s1,s2), которая принимает две строки и возвращает более длинную из них.
    Если длины строк равны, то вернуть первую из них.
    Создайте функцию longestStringLen(s1,s2), которая принимает две строки и возвращает длину более длинной из них.
    Если длины строк равны, то вернуть длину первой из них.
"""


def longestString(s1, s2):
    if len(s1) >= len(s2):
        return s1
    else:
        return s2


def longestStringLen(s1, s2):
    if len(s1) >= len(s2):
        return len(s1)
    else:
        return len(s2)



ts1 = ['Apple', '12345678', 'Dog', 'Spring']
ts2 = ['8765', 'Sport', 'Cat', 'Computer']

for i in range(len(ts1)):
    ls = longestString(ts1[i], ts2[i])
    lsl = longestStringLen(ts1[i], ts2[i])
    print(ts1[i], ts2[i], '->', ls, lsl)
