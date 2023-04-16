"""
Создайте класс Point, состоящий из двух полей х и у, которые предназначены для
хранения координат точки на плоскости. В классе создайте конструктор, принимающий
координаты точки и сохраняющий их в эти поля. Создайте логическую функцию
isInside 1, которая принимает объект класса Point и проверяет, попадает ли эта точка в
единичную окружность. При необходимости импортируйте библиотеки.
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def isInside1(o):
    if (o.x ** 2 + o.y ** 2) ** 0.5 <= 1:
        result = True
    else:
        result = False
    return result


def dist0(p1):
    result = ((p1.x ** 2) + (p1.y ** 2)) ** 0.5
    return result


points = list()
points.append(Point(1.1, 2.2))
points.append(Point(10, 20))
points.append(Point(0.5, 0.1))
points.append(Point(-0.7, 0.7))
points.append(Point(1, 1))
points.append(Point(0, 1))
points.append(Point(1, 0))
points.append(Point(1, 1))

for k in points:
    x = k.x
    y = k.y
    print("(%g, %g) -> %s" % (x, y, isInside1(k)))
