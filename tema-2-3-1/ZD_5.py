"""
Создайте логическую функцию isHappy, которая принимает в качестве аргумента шестизначный номер билета
и проверяет, является ли он счастливым. Билет является счастливым, если сумма его первых трех цифр
равна сумме трех последних.
"""


def isHappy(x):
    x = str(x)
    x1 = [int(i) for i in x[:len(x)//2]]
    x2 = [int(i) for i in x[len(x)//2:]]
    if sum(x1) == sum(x2):
        return True
    else:
        return False


ts = [123456, 123123, 111300, 111112, 123222, 555465, 100100, 987654, 301112, 444444]
for x in ts:
    if isHappy(x):
        print(x, "+")
    else:
        print(x, "-")

print()
for x in ts:
    print(x, isHappy(x))
