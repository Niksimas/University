"""
    Создайте класс Counter (счетчик), позволяющий инициализировать, увеличивать и уменьшать
    значение некоторого счетчика.
    Класс содержит поле step, по умолчанию равное 1. Класс должен соответствовать следующим требованиям:

    - конструктор принимает целое число, задающее начальное значение счетчика;
    - метод increment() увеличивает значение счетчика на величину шага;
    - метод decrement() уменьшает значение счетчика на величину шага;
    - метод getValue() возвращает текущее значение счетчика.

    Данные методы не принимают никаких аргументов.

    - метод setStep(step) устанавливает величину шага;
"""


class StepCounter:
    def __init__(self, num, step=1):
        self.num = num
        self.step = step

    def increment(self):
        self.num += self.step

    def decrement(self):
        self.num -= self.step

    def getValue(self):
        return self.num

    def setStep(self, value):
        self.step = value


c1 = StepCounter(100)
c1.increment()
c1.increment()
print(c1.getValue())
c1.decrement()
print(c1.getValue())
c1.setStep(10)
c1.increment()
c1.increment()
print(c1.getValue())
c1.decrement()
print(c1.getValue())
