"""
    Создайте класс Time, состоящий из трех полей: hours, minutes и seconds,
    которые предназначены для хранения часов, минут и секунд.
    В классе создайте конструктор, принимающий эти три значения и сохраняющий их в перечисленные поля класса.

    Создайте функцию getSeconds, которая принимает объект класса Time и возвращает время в секундах,
    соответствующее сохраненному в классе моменту времени.
"""


class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds


def getSeconds(obj):
    result = obj.seconds + obj.minutes * 60 + obj.hours * 3600
    return result


times = []
times.append(Time(0, 0, 59))
times.append(Time(1, 0, 0))
times.append(Time(1, 1, 1))
times.append(Time(12, 0, 0))
times.append(Time(10, 30, 0))
times.append(Time(12, 0, 0))
times.append(Time(10, 30, 0))

for t in times:
    print(getSeconds(t))
