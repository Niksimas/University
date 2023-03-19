def straight(x, y, z):
    spisok = [x, y, z]
    spisok.sort()
    print(spisok[0], spisok[1], spisok[2])


def reverse(x, y, z):
    spisok = [x, y, z]
    spisok.sort(reverse=True)
    print(spisok[0], spisok[1], spisok[2])


straight(123, 567, 1)
reverse(123, 567, 1)
straight(1, 2, 3)
reverse(1, 2, 3)