def dsum(x):
    num = list(str(x))
    s_num = 0
    for i in num:
        s_num += int(i)
    return s_num


numbers = [123128, 53412, 23335, 0, 1, 4, 20, 64, 100, 1000]
for x in numbers:
    print(x, "->", dsum(x))