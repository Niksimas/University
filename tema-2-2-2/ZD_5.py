def printGeometric(x, y, z):
    x= float(x)
    result = f"{x:.3f}"
    for i in range(z):
        x *= y
        result += f", {x:.3f}"
    result += "."
    print(result)


printGeometric(1, 2, 8)
printGeometric(1, 0.5, 8)
printGeometric(30, 0.99, 10)
printGeometric(2, 1.1, 10)
