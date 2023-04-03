"""
Создайте функцию addSeparator, которая принимает в качестве аргументов две строки
и возвращает символы первой строки через разделитель, равный второй строке.
"""


def addSeparator(st, sim):
    revers = [i for i in st]
    return f"{sim}".join(revers)



print(addSeparator('Apple', '*'))
print(addSeparator('12345678', '+'))
print(addSeparator('A', '&'))
print(addSeparator('XYZ', '&'))
print(addSeparator('xyz', ' = '))
print(addSeparator('ABCDEFG', ', '))
