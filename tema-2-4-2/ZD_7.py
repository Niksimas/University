def getHex(x):
    p = str(format(x, 'x'))
    result = ""
    for i in p:
        try:
            int(i)
            result += i
        except ValueError:
            result += i.upper()
    return result

ts = [10, 11, 12, 13, 14, 15, 16, 2033320, 2232300, 999999]
for x in ts:
    print(x, getHex(x))
