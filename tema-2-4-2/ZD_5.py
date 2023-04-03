def printPowers10(x):
    num = []
    for i in str(x):
        num.insert(0, i)
    print(f"{num[0]}*1", end="")
    for i in range(1, len(num)):
        print(f" + {num[i]}*1{'0'* i}", end="")
    print("")

ts = [1, 15, 123, 234, 34235, 3782000, 6400, 100022328, 9809877]
for x in ts:
    print(x, end=' = ')
    printPowers10(x)
