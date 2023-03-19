def hamming(x):
    p = bin(x)[2:]
    result = 0
    for i in p:
        if i == "1":
            result += 1
    return result


ts = [1, 15, 32, 456, 1000, 512, 999, 888, 511, 1023]
for x in ts:
    print("%5d %10s %2d" % (x, bin(x)[2:], hamming(x)))
