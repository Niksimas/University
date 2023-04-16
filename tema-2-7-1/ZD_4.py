"""
    Создайте класс Point, состоящий из двух полей x и y,
    предназначенных для хранения координат точки на плоскости.
    В классе создайте конструктор, принимающий координаты точки и сохраняющий их в эти поля.

    Создайте функцию dist0(p), которая принимает объект класса Point
    и возвращает расстояние от этой точки до начала координат. При необходимости импортируйте библиотеки.
"""


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


def dist0(p1):
    result = ((p1.x ** 2) + (p1.y ** 2)) ** 0.5
    return result


points = list()
points.append(Point(1.1, 2.2))
points.append(Point(10, 20))
points.append(Point(7, 0))
points.append(Point(0, 6))
points.append(Point(0, 0))
points.append(Point(3, 4))
points.append(Point(4, 3))

for p in points:
    print("dist0(%g, %g) = %.2f" % (p.x, p.y, dist0(p)))
