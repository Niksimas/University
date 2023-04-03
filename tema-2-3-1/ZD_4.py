"""
Создайте логическую функцию isInCircle, которая принимает в качестве аргументов два вещественных числа,
представляющие собой координаты точки на плоскости, и проверяет,
попадает ли эта точка внутрь единичного круга (True - попадает и False - не попадает).
Единичный круг - это круг радиуса 1 с центром в точке (0,0).
"""


def isInCircle(x, y):
    if (x ** 2) + (y ** 2) <= 1:
        return True
    else:
        return False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

pts = list()
pts.append(Point(0.5, 0.5))
pts.append(Point(2, 0.5))
pts.append(Point(-0.1, 0.7))
pts.append(Point(0.99, -0.99))
pts.append(Point(0.7, 0.7))
pts.append(Point(-0.9, -0.3))
pts.append(Point(0.99, 0.99))

for p in pts:
    print(p.x, p.y, 'IN' if isInCircle(p.x, p.y) else 'OUT')

print()
for p in pts:
    print(p.x, p.y, isInCircle(p.x, p.y))