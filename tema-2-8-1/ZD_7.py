"""
    Создайте класс BankAccount (банковский счет), позволяющий добавлять денежные средства на счет, снимать их и узнавать баланс (отрицательный баланс будет означать долг). Класс должен соответствовать следующим требованиям:

    - класс содержит поле balance, хранящее текущий баланс счета;
    - конструктор принимает начальный баланс счета и сохраняет его в поле balance;
    - метод topUp(summa) увеличивает balance на величину summa;
    - метод withdraw(summa) уменьшает balance на величину summa;
    - метод getBalance() возвращает значение balance.
"""


class BankAccount:
    def __init__(self, balance):
        self.balance = balance


    def topUp(self, summa):
        self.balance += summa

    def withdraw(self, summa):
        self.balance -= summa

    def getBalance(self):
        return self.balance


acc1 = BankAccount(100)
print(acc1.getBalance())
acc1.topUp(1)
acc1.topUp(2)
acc1.topUp(3)
print(acc1.getBalance())
acc1.withdraw(10)
acc1.withdraw(20)
acc1.withdraw(30)
print(acc1.getBalance())
acc1.topUp(400)
acc1.withdraw(400)
print(acc1.getBalance())
acc1.withdraw(46)
print(acc1.getBalance())
