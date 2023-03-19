def triangle2(N, S):
    sp=0
    s=1
    p=1
    while sp<2 and N>1:
        for l in range(s):
            print(S, end="")
        print()
        s+=1
        sp+=1
    while sp<N-1:
        print(S, end="")
        for i in range(p):
            print(" ", end="")
        print(S)
        p+=1
        sp+=1
        
    if sp==N-1:
        print(S*N)


triangle2(1, "*")
print()
triangle2(2, "=")
print()
triangle2(3, "W")
print()
triangle2(4, "%")
print()
triangle2(5, "!")
print()
triangle2(6, "6")
print()
triangle2(7, "7")
