"""
    Создайте класс Square, предназначенный для вывода квадрата из символов.
    Класс должен соответствовать следующим требованиям:

    - класс содержит два поля symbol и size, хранящие соответственно символ-заполнитель и размер квадрата;
    - конструктор присваивает параметры по умолчанию symbol='*' и size=10;
    - метод setSymbol(newSymbol) устанавливает новый заполнитель;
    - метод setSize(newSize) устанавливает новый размер;
    - метод printFigure() выводит квадрат с заданными параметрами.
"""


class Square:
    def __init__(self, symbol='*', size=10):
        self.symbol = symbol
        self.size = size

    def setSymbol(self, symbol):
        self.symbol = symbol

    def setSize(self, size):
        self.size = size

    def printFigure(self):
        print(f"{self.symbol * self.size}\n" * self.size, end="")


sq = Square()
sq.printFigure()
print()
sq.setSymbol('+')
sq.setSize(5)
sq.printFigure()
print()
sq.setSize(3)
sq.printFigure()