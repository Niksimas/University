def nsum(x):
    p = 0
    for i in range(x+1):
        p += i
    return p


numbers = [0, 1, 2, 3, 4, 5, 10, 20, 100]
for x in numbers:
    print(x, "->", nsum(x))
