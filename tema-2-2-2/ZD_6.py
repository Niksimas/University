def triangle(N, S):
    p=N-1
    s=1
    for k in range(N):
        for i in range(p):
            print(" ", end="")
        for l in range(s):
            print(S, end="")
        print()
        p-=1
        s+=1
