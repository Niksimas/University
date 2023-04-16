"""
Создайте класс Point, состоящий из двух полей x и у, которые
предназначены для хранения координат точки на плоскости.
В классе создайте конструктор, принимающий координаты точки и
сохраняющий их в эти поля.

Создайте класс Triangle(треугольник), состоящий из трех полей v1, v2, v3 типа Point, задающих координаты вершин этого
треугольника. В классе создайте конструктор, принимающий три
точки и сохраняющий их в поля класса.

Создайте функцию square, которая принимает объект класса
Triangle и возвращает площадь этого треугольника.
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3


def tsquare(obj):
    result = ((obj.p2.x - obj.p1.x)*(obj.p3.y - obj.p1.y) -
              (obj.p3.x - obj.p1.x)*(obj.p2.y - obj.p1.y))/2
    if result < 0:
        result *= -1
    return result


p1 = Point(1,0)
p2 = Point(0,0.322)
p3 = Point(0,0)
tr1 = Triangle(p1, p2, p3)
print("Square = %.3f" % tsquare(tr1))
q1 = Point(1,0)
q2 = Point(0,1.2441)
q3 = Point(10,3)
tr2 = Triangle(q1, q2, q3)
print("Square = %.3f" % tsquare(tr2))
