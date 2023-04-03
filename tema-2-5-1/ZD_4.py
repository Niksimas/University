"""
Создайте процедуру printDivisors, которая принимает в качестве аргумента целое число
и выводит все его делители в порядке возрастания через запятую с пробелом, а в конце ставит точку.
"""


def printDivisors(x):
    for i in range(1, x + 1):
        if x % i == 0:
            delit = i
            if i == 1:
                print(delit, end="")
            else:
                print(f", {delit}", end="")
    print(".")


for i in range(1, 23):
    print(str(i) + ": ", end="")
    printDivisors(i)
