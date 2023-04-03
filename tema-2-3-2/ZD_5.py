"""
Создайте логическую функцию isPower,
которая принимает в качестве аргументов два целых числа и проверяет,
является ли первое из них целой степенью второго.
"""



def isPower(x, y):
    x_l = [y**i for i in range(10)]
    if x in x_l:
        return True
    else:
        return False


numbers = [1, 2, 3, 4, 5, 8, 9, 12, 16, 25, 27, 30, 32, 81, 200]
print("Powers of 2:")
for x in numbers:
    if isPower(x, 2):
        print(x)

print("Powers of 3:")
for x in numbers:
    if isPower(x, 3):
        print(x)

print("Powers of 4:")
for x in numbers:
    if isPower(x, 4):
        print(x)

print("Powers of 5:")
for x in numbers:
    if isPower(x, 5):
        print(x)
