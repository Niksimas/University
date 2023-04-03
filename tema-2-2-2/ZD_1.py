def printArithmetic(x,y,z):
    x= float(x)
    result = f"{x}"
    for i in range(z):
        x += y
        result += f", {x:.1f}"
    result += "."
    print(result, end="")


printArithmetic(1, -2, 8)
print()
printArithmetic(1, 0.5, 8)
print()
printArithmetic(30, 0.99, 10)
print()
printArithmetic(2, 1.1, 10)
