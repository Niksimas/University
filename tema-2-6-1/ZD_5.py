"""
Создайте процедуру printWithSeparator,
 которая принимает в качестве аргументов две строки и
 выводит символы первой строки через разделитель, равный второй строке.
"""


def printWithSeparator(st, sim):
    revers = [i for i in st]
    print(f"{sim}".join(revers))


printWithSeparator('Apple', '*')
printWithSeparator('12345678', '+')
printWithSeparator('A', '&')
printWithSeparator('XYZ', '&')
printWithSeparator('xyz', ' = ')
printWithSeparator('ABCDEFG', ', ')
