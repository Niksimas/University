def getBinary(x):
    return format(x, 'b')

ts = [123321, 33, 555555555555555, 11, 65, 99, 100100, 23, 6, 0, 31]
for x in ts:
    print(x, getBinary(x))
