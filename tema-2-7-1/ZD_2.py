"""
    Создайте класс Time, состоящий из трех полей: hours, minutes и seconds,
    которые предназначены для хранения часов, минут и секунд.

    В классе создайте конструктор, принимающий эти три значения и сохраняющий их в перечисленные поля класса.

    Создайте функцию getPeriod(t1, t2), которая принимает два объекта класса Time и возвращает другой объект Time,
    означающий промежуток времени, который прошел от t1 до t2.
"""


class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds


def getPeriod(t1, t2):
    h = t2.hours - t1.hours
    m = t2.minutes - t1.minutes
    s = t2.seconds - t1.seconds
    while True:
        if s < 0:
            m -= 1
            s += 60
        elif m < 0:
            h -= 1
            m += 60
        else:
            break
    return Time(h, m, s)


times = []
times.append(Time(0, 0, 59))
times.append(Time(1, 0, 0))
times.append(Time(1, 1, 1))
times.append(Time(12, 0, 0))
times.append(Time(10, 30, 0))
times.append(Time(12, 0, 0))
times.append(Time(10, 30, 0))

for t in times:
    p = getPeriod(Time(0, 0, 59), t)
    print(p.hours, p.minutes, p.seconds)
