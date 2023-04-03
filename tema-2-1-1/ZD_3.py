def fsum(x, y):
    return x + y


def fmult(x, y):
    return x * y


def fmod(x, y):
    return x % y


def fsubtr(x, y):
    return x - y


x = [12, 100, 56, 78]
y = [3, 5, 7, 10]
for i in range(4):
    print(x[i], y[i])
    print('fsum = ', fsum(x[i], y[i]))
    print('fmult = ', fmult(x[i], y[i]))
    print('fmod = ', fmod(x[i], y[i]))
    print('fsubtr = ', fsubtr(x[i], y[i]))
    print()