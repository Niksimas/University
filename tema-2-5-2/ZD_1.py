"""
Создайте процедуру printEuclid(a,b), которая выводит через пробел последовательность
промежуточных вычислений при выполнении алгоритма Евклида для вычисления наибольшего общего делителя
двух чисел (см. примеры). После вывода перевести курсор на новую строку"""


def printEuclid(a, b):
    numb = [a, b]
    numb.sort()
    if a > b:
        print(a, end=" ")
    else:
        print(b, end=" ")
    i = 0
    while True:
        if numb[i] % numb[i + 1] != 0:
            print(numb[i] % numb[i + 1], end=" ")
            numb.append(numb[i] % numb[i + 1])
            i += 1
        else:
            print(0)
            break



printEuclid(30, 15)
printEuclid(15, 30)
printEuclid(120, 74)
printEuclid(74, 120)
printEuclid(45, 12)
printEuclid(12, 45)