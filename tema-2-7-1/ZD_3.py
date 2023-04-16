"""
    Создайте класс Point, состоящий из двух полей x и y,
    которые предназначены для хранения координат точки на плоскости.
    В классе создайте конструктор, принимающий координаты точки и сохраняющий их в эти поля.

    Создайте функцию distance, которая принимает два объекта класса Point и возвращает расстояние между этими точками.
    При необходимости импортируйте библиотеки.
"""


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1, p2):
    result = (((p2.x - p1.x) ** 2) + ((p2.y - p1.y) ** 2)) ** 0.5
    return result


points = list()
points.append(Point(1, 0))
points.append(Point(2, 0))
points.append(Point(0, 4))
points.append(Point(0, 5))
points.append(Point(2.6, 3.1))
points.append(Point(4.3, 6.7))
points.append(Point(4, 3))
points.append(Point(0, 0))

for i in range(len(points)):
    for j in range(i+1, len(points)):
        p1 = points[i]
        p2 = points[j]
        d = distance(p1, p2)
        print("point1=(%.2f, %.2f) point2=(%.2f, %.2f) distance=%.2f" % (p1.x, p1.y, p2.x, p2.y, d))
