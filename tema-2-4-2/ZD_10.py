def hammingDistance(x, y):
    X = list(bin(x)[2:])
    Y = list(bin(y)[2:])
    result = 0
    if len(X) > len(Y):
        while len(X) != len(Y):
            Y.insert(0, "0")
    if len(X) < len(Y):
        while len(X) != len(Y):
            X.insert(0, "0")
    for i in range(len(X)):
        if X[i] != Y[i]:
            result += 1
    return result


ts = [1, 15, 32, 456, 1000, 512, 999, 888, 511, 1023]
print("%4s %4s %10s %10s %s" % ('x', 'y', 'binx', 'biny', 'HamDist'))
for i in range(len(ts)):
    for j in range(len(ts)):
        if i>=j:
            x = ts[i]
            y = ts[j]
            bx = bin(x)[2:]
            by = bin(y)[2:]
            hd = hammingDistance(x,y)
            print("%4d %4d %10s %10s %2d" % (x, y, bx, by, hd))