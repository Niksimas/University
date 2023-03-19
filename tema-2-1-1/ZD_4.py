def fs(v, t):
    return v * t


def fv(s, t):
    return s / t


def ft(s, v):
    return s / v

ss = [10, 20, 30]
vs = [3.34, 5.76, 4, 7]
ts = [1.04, 2.33, 5.112]

for v in vs:
    for t in ts:
        print("%.2f %.2f -> %.2f" % (v, t, fs(v, t)))

for s in vs:
    for t in ts:
        print("%.2f %.2f -> %.2f" % (s, t, fv(s, t)))

for s in vs:
    for v in ts:
        print("%.2f %.2f -> %.2f" % (s, v, ft(s, v)))