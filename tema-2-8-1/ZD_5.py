"""
    Создайте класс Hero (герой), моделирующий перемещение героя компьютерной игры по координатной плоскости.
    Герой начинает свое движение в начале координат (точка - 0,0) и может двигаться на одну позицию вправо,
    влево, вверх и вниз. Класс должен соответствовать следующим требованиям:

    - класс содержит два поля x и y, хранящие текущие координаты героя;
    - конструктор присваивает текущим координатам (0,0);
    - метод moveRight() увеличивает x на единицу;
    - метод moveLeft() уменьшает x на единицу;
    - метод moveUp() увеличивает y на единицу;
    - метод moveDown() уменьшает y на единицу;
    - метод getX() возвращает x;
    - метод getY() возвращает y.
"""


class Hero:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def moveRight(self):
        self.x += 1

    def moveLeft(self):
        self.x -= 1

    def moveUp(self):
        self.y += 1

    def moveDown(self):
        self.y -= 1

    def getX(self):
        return self.x

    def getY(self):
        return self.y


hero1 = Hero()
print(hero1.getX(), hero1.getY())
hero1.moveDown()
hero1.moveDown()
hero1.moveDown()
hero1.moveRight()
print(hero1.getX(), hero1.getY())
hero1.moveUp()
hero1.moveDown()
hero1.moveRight()
hero1.moveLeft()
print(hero1.getX(), hero1.getY())
hero1.moveLeft()
hero1.moveLeft()
hero1.moveLeft()
hero1.moveLeft()
hero1.moveLeft()
hero1.moveUp()
hero1.moveUp()
hero1.moveUp()
hero1.moveUp()
print(hero1.getX(), hero1.getY())