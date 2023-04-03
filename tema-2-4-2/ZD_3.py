def isSymmetric2(x):
    xb = bin(x)[2:]
    par = len(xb) - 1
    for i in range(len(xb)):
        if xb[i] == xb[par]:
            par -= 1
            result = True
        else:
            result = False
            break
    return result


ts1 = [123321, 33, 555555555555555, 11, 65, 99, 100100, 23, 6, 0, 31]
print("Symmetric:")
for x in ts1:
    if isSymmetric2(x):
        print(x, bin(x)[2:])

ts2 = [234, 43, 112233445566, 432, 565, 556655, 87654, 45454, 3334, 23]
print()
print("Not symmetric:")
for x in ts2:
    if not isSymmetric2(x):
        print(x, bin(x)[2:])

print()
for x in ts1:
    print(x, bin(x)[2:], isSymmetric2(x))
