"""
Создайте функцию changeRegister, которая принимает в качестве аргумента строку и возвращает строку,
где заглавные буквы исходной строки преобразованы в строчные, а строчные - в заглавные.
"""


def changeRegister(a):
    return a.swapcase()


ts = ['Apple', 'TABLE', 'orange', 'yeaR', 'SPEaker']

for s in ts:
    print(changeRegister(s))