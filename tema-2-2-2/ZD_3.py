def printNumbers(x, y):
    for i in range(1, x):
        print(f"{i}{y}", end="")
    print(x)

printNumbers(15, "*")
printNumbers(10, ", ")
printNumbers(1, "***")
printNumbers(2, "***")
printNumbers(7, " + ")
