def printPowers10v2(x):
    num = []
    statys = ""
    for i in str(x):
        num.insert(0, i)
    if len(num) == 1:
        print(f"{num[0]}*1", end="")
    else:
        if num[0] != "0":
            print(f"{num[0]}*1", end="")
            statys = "y"
        for i in range(1, len(num)):
            if (statys == "y") and (num[i] != "0"):
                print(" + ", end="")
            if num[i] != "0":
                print(f"{num[i]}*1{'0'* i}", end="")
                statys = "y"
    print("")

ts = [12345, 15, 1203, 20304, 34020305, 3782000, 6400, 100022328, 9809877, 98765]
for x in ts:
    print(x, end=' = ')
    printPowers10v2(x)
