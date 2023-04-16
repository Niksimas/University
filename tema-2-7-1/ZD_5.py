"""
    Создайте класс Point, состоящий из двух полей x и y,
    которые предназначены для хранения координат точки на плоскости.
    В классе создайте конструктор, принимающий координаты точки и сохраняющий их в эти поля.

    Создайте функцию isInside, которая принимает объект класса Point и проверяет,
    попадает ли он внутрь единичного квадрата.
    Единичный квадрат ограничен точками (1,1), (-1,1), (-1,-1), (1,-1).
    При необходимости импортируйте библиотеки.
"""


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


def isInside(p):
    if (p.x < 1) and (p.x > -1) and (p.y < 1) and (p.y > -1):
        result = True
    else:
        result = False
    return result


points = list()
points.append(Point(0.99, 0.99))
points.append(Point(2, 0))
points.append(Point(0, 0))
points.append(Point(0.6, 0.5))
points.append(Point(0.6, 0.1))
points.append(Point(2, 0))
points.append(Point(0, 2))
points.append(Point(1, 1))

for p in points:
    print(p.x, p.y, isInside(p))
