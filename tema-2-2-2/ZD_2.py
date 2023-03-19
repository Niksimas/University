def printNumbers(x, y):
    print(x, end="")
    if x < y:
        for i in range(x+1, y +1):
            print(f", {i}", end="")
    else:
        for i in range(x - 1, y-1, -1):
            print(f", {i}", end="")
    print(".", end="")

printNumbers(1, 10)
print()
printNumbers(10, 1)
print()
printNumbers(5, 5)
print()
printNumbers(100, 90)
print()
printNumbers(100, 109)
