def powers2(x):
    s = 0
    l = 0
    lists = []

    while s < x:
        s = 2 ** l
        l = l + 1
    if s == x:
        lists.append(s)
    else:
        while x > 0:
            for i in range(l):
                if 2 ** i > x:
                    x = x - (2 ** (i - 1))
                    lists.append(2 ** (i - 1))
                    break
    lists.sort()
    summ = str(lists[0])
    for i in range(1, len(lists)):
        summ += f" + {lists[i]}"
    return summ


ts = [1, 15, 123, 234, 345, 32, 64, 128, 987]
for x in ts:
    print(x, '=', powers2(x))
