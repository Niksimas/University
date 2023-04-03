def triangle(n,s,reverse):
    if reverse == True:
        for i in range(n):
            print(n * s)
            n -= 1
    else:
        p = 1
        for i in range(n):
            print(p * s)
            p += 1

triangle(7, '*', False)
triangle(5, '%', True)
triangle(9,'$',False)
