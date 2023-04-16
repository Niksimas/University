"""
    Создайте класс Arithmetic, предназначенный вывода арифметической прогрессии.
    Числа последовательности должны разделяться и заканчиваться заданными строками.
    Класс должен иметь возможность изменять эти строки.
    Класс должен соответствовать следующим требованиям:

    - класс содержит два поля a0 (первый элемент), step (шаг прогрессии), separator и last,
        хранящие соответственно разделитель и окончание;
    - конструктор присваивает параметры по умолчанию a0 = 1, step = 1, separator=', ' и last='.';
    - метод setSeparator(newSeparator) устанавливает новый разделитель;
    - метод setLast(newLast) устанавливает новую строку для окончания;
    - метод printNumbers() выводит прогрессию с заданными параметрами,
        где числа разделены разделителем и заканчиваются строкой last.
"""


class Arithmetic:
    def __init__(self, a0=1, step=1, N=10, separator=", ", last="."):
        self.first = a0
        self.step = step
        self.N = N
        self.separator = separator
        self.last = last

    def setSeparator(self, newSeparator):
        self.separator = newSeparator

    def setLast(self, newLast):
        self.last = newLast

    def setN(self, newN):
        self.N = newN

    def setStep(self, newStep):
        self.step = newStep

    def printNumbers(self):
        num = [self.first]
        for i in range(self.N - 1):
            num.append(num[i] + self.step)
        print(*num, sep=self.separator, end=f"{self.last}\n")


ar1 = Arithmetic()
ar1.printNumbers()
ar1.setN(5)
ar1.setStep(3)
ar1.setSeparator(' + ')
ar1.setLast(' = ?')
ar1.printNumbers()
