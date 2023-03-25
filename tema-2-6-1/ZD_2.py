"""
    Создайте функцию reversedString(s), которая принимает в качестве аргумента строку и
    возвращает ее в обратном порядке (см. примеры).
"""


def reversedString(s):
    revers = []
    for i in s:
        revers.insert(0, i)
    return "".join(revers)


ts = ['R', 'Computer', '1122334455']
for t in ts:
    print(t, '->', reversedString(t))
