"""
    Создайте класс Point, состоящий из двух полей x и y,
    которые предназначены для хранения координат точки на плоскости.
    В классе создайте конструктор, принимающий координаты точки и сохраняющий их в эти поля.
    В классе создайте метод dist0, который возвращает расстояние от этой точки до начала координат.
    При необходимости импортируйте библиотеки.
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist0(self):
        result = ((self.x ** 2) + (self.y ** 2)) ** 0.5
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
    print(p.dist0())
