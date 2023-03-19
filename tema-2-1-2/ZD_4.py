def fib(x):
    fib_num = [0, 1, 1]
    try:
        result = fib_num[x]
    except IndexError:
        for i in range(2, x):
            fib_num.append(fib_num[i-1] + fib_num[i])
        result = fib_num[x]
    print(fib_num)
    return result


for i in range(0, 15):
    print(i, fib(i))