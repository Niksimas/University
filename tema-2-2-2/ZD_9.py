def triangle(N, S):
    s=1
    for k in range(N):
        for l in range(s):
            print(S, end="")
        print()
        s+=1
            

triangle(1, "*")
print()
triangle(2, "+")
print()
triangle(3, "%")
print()
triangle(4, "!")
