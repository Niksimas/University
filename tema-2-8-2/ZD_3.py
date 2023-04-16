"""
    Создайте класс StringFormatter, предназначенный форматирования строки специальным образом.
    Символы строки должны быть разделяться и заканчиваться заданными строками.
    Класс должен иметь возможность изменять эти строки. Класс должен соответствовать следующим требованиям:

    - класс содержит два поля separator и last, хранящие соответственно разделитель и окончание;
    - конструктор присваивает параметры по умолчанию separator=', ' и last='.';
    - метод setSeparator(newSeparator) устанавливает новый разделитель;
    - метод setLast(newLast) устанавливает новую строку для окончания;
    - метод formatString(s) возвращает строку, где символы разделены разделителем и заканчиваются строкой last.
"""


class StringFormatter:
    def __init__(self, separator=", ", last="."):
        self.separator = separator
        self.last = last

    def setSeparator(self, newSeparator):
        self.separator = newSeparator

    def setLast(self, newLast):
        self.last = newLast

    def formatString(self, s):
        num = list(s)
        result = ""
        for i in range(len(num) - 1):
            result += num[i] + self.separator
        result += num[-1] + self.last
        return result


form1 = StringFormatter()
print(form1.formatString('12345'))
print(form1.formatString('apple'))
form2 = StringFormatter()
form2.setSeparator(' + ')
form2.setLast(' = ?')
"""print(form2.formatString('12345'))
print(form2.formatString('9876'))"""
