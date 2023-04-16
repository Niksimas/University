"""
   Создайте класс Printer, предназначенный для печати символа заданное количество раз.
   По умолчанию печатается звездочка один раз.
   Класс должен иметь возможность изменять печатаемый символ и количество печатаемых символов.
   Класс должен соответствовать следующим требованиям:

    - класс содержит два поля symbol и number, хранящие соответственно печатаемый символ и количество символов;
    - конструктор присваивает параметры по умолчанию symbol='*' и number=1;
    - метод setSymbol(symbol) устанавливает новый символ для печати;
    - метод setNumber(number) устанавливает количество печатаемых сомволов;
    - метод printSymbols() печатает установленный символ установленное количество раз.
"""


class Printer:
    def __init__(self, symbol='*', number=1):
        self.symbol = symbol
        self.number = number

    def setSymbol(self, symbol):
        self.symbol = symbol

    def setNumber(self, number):
        self.number = number

    def printSymbols(self):
        print(self.symbol * self.number)


printer1 = Printer()
printer1.printSymbols()
printer1.setSymbol('+')
printer1.printSymbols()
printer1.setNumber(10)
printer1.printSymbols()
printer1.setSymbol('7')
printer1.setNumber(12)
printer1.printSymbols()