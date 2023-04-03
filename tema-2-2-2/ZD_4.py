def printFib(x):
    fib_num = [0, 1]
    result = "0"
    for i in range(1, x):
        fib_num.append(fib_num[i-1] + fib_num[i])
    fib_num.pop(0)
    fib_num.pop(len(fib_num)-1)
    for i in fib_num:
        result += f", {i}"
    print(result)


printFib(1)
printFib(3)
printFib(5)
printFib(7)
printFib(2)
printFib(4)
printFib(6)
