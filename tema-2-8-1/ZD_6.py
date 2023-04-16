"""
    Создайте класс Hero (герой), моделирующий перемещение героя компьютерной игры по координатной плоскости.
    Герой начинает свое движение в начале координат (точка - 0,0)
    и может двигаться на одну позицию вправо, влево, вверх и вниз.
    Дополнительно должна быть возможность изменения шага перемещения.
    Класс должен соответствовать следующим требованиям:

    - класс содержит три поля x и y, хранящие текущие координаты героя, а также поле step - размер шага перемещения;
    - конструктор присваивает текущим координатам (0,0) и step = 1;
    - метод moveRight() увеличивает x на величину шага;
    - метод moveLeft() уменьшает x на величину шага;
    - метод moveUp() увеличивает y на величину шага;
    - метод moveDown() уменьшает y на величину шага;
    - метод getX() возвращает x;
    - метод getY() возвращает y;
    - метод setStep(step) устанавливает величину шага, указанную в аргументе метода.
"""


class Hero:
    def __init__(self, x=0, y=0, step=1):
        self.x = x
        self.y = y
        self.step = step

    def moveRight(self):
        self.x += self.step

    def moveLeft(self):
        self.x -= self.step

    def moveUp(self):
        self.y += self.step

    def moveDown(self):
        self.y -= self.step

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setStep(self, value):
        self.step = value


hero1 = Hero()
print(hero1.getX(), hero1.getY())
hero1.moveDown()
hero1.moveDown()
print(hero1.getX(), hero1.getY())
hero1.moveDown()
hero1.moveRight()
print(hero1.getX(), hero1.getY())
hero1.setStep(2)
hero1.moveUp()
print(hero1.getX(), hero1.getY())
hero1.moveDown()
hero1.moveRight()
hero1.moveLeft()
print(hero1.getX(), hero1.getY())
hero1.setStep(3)
hero1.moveLeft()
hero1.moveLeft()
hero1.setStep(100)
hero1.moveLeft()
hero1.moveLeft()
hero1.moveLeft()
print(hero1.getX(), hero1.getY())
hero1.setStep(5)
hero1.moveUp()
hero1.moveUp()
print(hero1.getX(), hero1.getY())
hero1.setStep(1000)
hero1.moveUp()
hero1.moveUp()
print(hero1.getX(), hero1.getY())