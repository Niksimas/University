def fsum(x, y):
    return x + y


for i in range(5):
    for j in range(5, 10):
        print(i, '+', j, '=', fsum(i, j))
