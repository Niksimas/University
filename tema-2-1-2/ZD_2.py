def fact(x):
    p = 1
    for i in range(1, x + 1):
        p *= i
    return p


numbers = [0, 1, 2, 3, 7, 11]
for x in numbers:
    print(x, "->", fact(x))
