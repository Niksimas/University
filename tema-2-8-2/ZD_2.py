"""
    Игра в города заключается в том, что участники по очереди называют слова (города),
    начинающиеся с буквы, на которую заканчивается слово, названное предыдущим участником.

    Создайте класс CitiesGame, позволяющий реализовать игру в города программно.
    Класс должен реализовывать следующие два метода:

    - метод addWord(word) принимает в качестве аргумента слово и проверяет,
        можно ли добавить слово согласно указанным правилам, а затем добавляет (если это возможно),
        возвращая True, либо False - если добавить невозможно;
    - метод printAllWords() выводит на консоль все добавленные слова, разделяя их пробелами, в порядке их добавления.

    Данные методы не принимают никаких аргументов.
"""


class CitiesGame:
    def __init__(self):
        self.AllWords = []

    def addWord(self, newWord):
        try:
            if self.AllWords[-1][-1] == newWord[0]:
                self.AllWords.append(newWord)
                return True
            else:
                return False
        except IndexError:
            self.AllWords.append(newWord)
            return True

    def printAllWords(self):
        print(*self.AllWords, sep=" ")


game1 = CitiesGame()
words = ['apple', 'eagle', 'exit', 'trial', 'letter', 'rythm', 'monkey', 'yard']
for word in words:
    print(word, 'YES' if game1.addWord(word) else 'NO')
print()
game1.printAllWords()
print()
game2 = CitiesGame()
words = ['apple', 'town', 'exit', 'rabbit', 'teacher', 'city', 'round', 'dwarf']
for word in words:
    print(word, 'YES' if game2.addWord(word) else 'NO')
print()
game2.printAllWords()
