def nfib(x):
    fib_num = [0, 1, 1]
    for i in range(2, x+1):
        fib_num.append(fib_num[i - 1] + fib_num[i])
    if x in fib_num:
        result = fib_num.index(x)
    else:
        result = -1
    return result

for i in range(25):
    print("%2d: %2d" % (i, nfib(i)))
