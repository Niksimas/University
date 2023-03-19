def numbers(x, y):
    if x > y:
        for i in range(x, y - 1, -1):
            print(x, end=" ")
            x -= 1
        print()
    else:
        for i in range(x, y + 1, 1):
            print(x, end=" ")
            x += 1
        print()


numbers(10, 20)
numbers(20, 10)
numbers(-10, 10)
numbers(10, -10)
