def printExpression(x, y, z):
    if z == "+":
        print(f"{x} + {y} = {x + y}")
    elif z == "-":
        print(f"{x} - {y} = {x - y}")
    elif z == "*":
        print(f"{x} * {y} = {x * y}")
    elif z == "DIV":
        print(f"{x} DIV {y} = {x // y}")
    elif z == "MOD":
        print(f"{x} MOD {y} = {x % y}")


printExpression(10, 20, '+')
printExpression(100, 12, '-')
printExpression(1000, 1000, '*')
printExpression(11, 5, 'DIV')
printExpression(11, 5, 'MOD')
