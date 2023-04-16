"""
    Создайте класс Counter (счетчик), позволяющий инициализировать, увеличивать и уменьшать
    значение некоторого счетчика. Класс должен соответствовать следующим требованиям:

    - конструктор принимает целое число, задающее начальное значение счетчика;
    - метод increment() увеличивает значение счетчика на единицу;
    - метод decrement() уменьшает значение счетчика на единицу;
    - метод getValue() возвращает текущее значение счетчика.

    Данные методы не принимают никаких аргументов.
"""


class Counter:
    def __init__(self, num):
        self.num = num

    def increment(self):
        self.num += 1

    def decrement(self):
        self.num -= 1

    def getValue(self):
        return self.num



c1 = Counter(1)
c1.increment()
c1.increment()
c1.increment()
print("Counter1 =", c1.getValue())

c2 = Counter(1000)
for i in range(57):
    c2.decrement()
print("Counter2 =", c2.getValue())

c3 = Counter(20)
c3.increment()
c3.increment()
c3.increment()
c3.decrement()
c3.decrement()
print("Counter3 =", c3.getValue())