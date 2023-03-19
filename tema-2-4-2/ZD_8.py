def getDec(x):
    result = int(x, 16)
    return result

ts = ['A', 'B12', 'C654', 'f0ff0f', 'A1A1BB1CC', 'a0b0c0d']
for x in ts:
    print(x, getDec(x))
