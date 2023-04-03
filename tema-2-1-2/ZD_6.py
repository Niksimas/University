import math


def npow2(t):
    m = math.log2(t)
    print(m, m%1)
    if m % 10 == 0:
        result = int(m)
    else:
        result = -1
    return result

ts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 16, 32, 64, 100, 128]

for t in ts:
    print("%3d %2d" % (t, npow2(t)))
