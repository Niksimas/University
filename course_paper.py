"""
Разработайте консольное приложение для работы со списком объектов согласно своему варианту.
Объект характеризуется 4 свойствами (свойства перечислены в варианте).

Создайте массив, который может содержать не более 12 объектов. Это означает, что при попытке добавить 13-ый объект
сообщается о невозможности это сделать.
При запуске программы уже должно содержаться 5 объектов, добавленных предварительно в программном коде.
Приложение предполагает работу меню из следующих пунктов:
    Вывод всех объектов в виде таблицы.
    Выход из программы.
    Добавление нового объекта (значения свойств ввести с клавиатуры).
    Удаление выбранного пользователем объекта.
    Сортировка объектов по выбранному пользователем свойству.
    Фильтрация (вывод объектов с указанным свойством) – согласно варианту.
    Преобразование значения свойства у всех объектов – согласно варианту.
"""

import subprocess
import sys

try:
    from prettytable import PrettyTable
except ModuleNotFoundError:
    package = 'PrettyTable'
    print(f"Внимание! Будет установлен недостающий модуль \"{package}\"")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])


class Star:
    def __init__(self, constellation, distance, weight):
        self.constellation = constellation
        self.distance = distance
        self.weight = weight


th = ["Название", "Созвездие", "Расстояние от Солнца (в св.г.)", "Масса (в массах Солнца)"]

star_dict = {"Сириус": Star("Большой Пёс", 9, 2), "Поллукс": Star("Близнецы", 34, 2), "Арктур": Star("Волопас", 37, 1),
             "Антарес": Star("Скорпион", 550, 13), "Бетельгейзе": Star("Орион", 548, 19)}


def convert_obj():
    """Вывод расстояния до всех звезд в парсеках вместо световых лет"""
    th1 = ["Название", "Созвездие", "Расстояние от Солнца (в парсеках)", "Масса (в массах Солнца)"]
    columns = len(th1)
    table = PrettyTable(th1)
    td_data = []
    for i in star_dict:
        td_data.append(i)
        td_data.append(star_dict[i].constellation)
        td_data.append(round(star_dict[i].distance * 0.306, 2))
        td_data.append(star_dict[i].weight)
    while td_data:
        table.add_row(td_data[:columns])
        td_data = td_data[columns:]
    print(table)


def filter_obj():
    """Вывод всех звезд, у которых масса не превосходит заданной величины"""
    columns = len(th)
    table = PrettyTable(th)
    td_data = []
    while True:
        try:
            weight_user = int(input("Задайте фильтр по массе (целое число): "))
            break
        except ValueError:
            print("Данные не являются целым числом. Попробуйте ещё раз.")
    for i in star_dict:
        if star_dict[i].weight <= weight_user:
            td_data.append(i)
            td_data.append(star_dict[i].constellation)
            td_data.append(star_dict[i].distance)
            td_data.append(star_dict[i].weight)
    while td_data:
        table.add_row(td_data[:columns])
        td_data = td_data[columns:]
    print(table)


def sorting_selection():
    while True:
        par_sort = input("Сортировать по возрастанию или убыванию? (+/-): ")
        if par_sort in ["+", "-"]:
            break
        else:
            print("Неизвестный параметр! Укажите \"+\" - возрастание или \"-\" - убывание.")
    if par_sort == "+":
        par_sort = False
    else:
        par_sort = True
    return par_sort


def weight_sort():
    par_sort = sorting_selection
    keys = list(star_dict.keys())
    part_star_dict = {}
    for i in keys:
        part_star_dict[i] = star_dict[i].weight

    sorted_dict = {}
    sorted_keys = sorted(part_star_dict, key=part_star_dict.get, reverse=par_sort())

    for w in sorted_keys:
        sorted_dict[w] = part_star_dict[w]
    list_obj(list(sorted_dict.keys()))


def distance_sort():
    par_sort = sorting_selection
    keys = list(star_dict.keys())
    part_star_dict = {}
    for i in keys:
        part_star_dict[i] = star_dict[i].distance

    sorted_dict = {}
    sorted_keys = sorted(part_star_dict, key=part_star_dict.get, reverse=par_sort())

    for w in sorted_keys:
        sorted_dict[w] = part_star_dict[w]
    list_obj(list(sorted_dict.keys()))


def constellation_sort():
    par_sort = sorting_selection
    keys = list(star_dict.keys())
    part_star_dict = {}
    for i in keys:
        part_star_dict[i] = star_dict[i].constellation

    sorted_dict = {}
    sorted_keys = sorted(part_star_dict, key=part_star_dict.get, reverse=par_sort())

    for w in sorted_keys:
        sorted_dict[w] = part_star_dict[w]
    list_obj(list(sorted_dict.keys()))


def name_sort():
    name = list(star_dict.keys())
    par_sort = sorting_selection
    name.sort(reverse=par_sort())
    list_obj(name)


def sort_obj():
    while True:
        try:
            par_sort = input("Выберите параметр сортировки (название/созвездие/расстояние/масса): ")
            dict_sort = {"название": name_sort, "созвездие": constellation_sort,
                         "расстояние": distance_sort, "масса": weight_sort}
            dict_sort[par_sort.split(" ")[0]]()
            break
        except KeyError:
            print("Нет такого параметра!")


def list_obj(name: list = None):
    columns = len(th)
    table = PrettyTable(th)
    td_data = []
    if name is None:
        key = star_dict
    else:
        key = name
    for i in key:
        td_data.append(i)
        td_data.append(star_dict[i].constellation)
        td_data.append(star_dict[i].distance)
        td_data.append(star_dict[i].weight)
    while td_data:
        table.add_row(td_data[:columns])
        td_data = td_data[columns:]
    print(table)


def del_obj():
    print("Вы вошли в режим удаления небесных тел.\n")
    key = star_dict.keys()
    print("Звезды которые можно удалить:  ")
    for i in key:
        print(f"{i}", end="  ")
    print()
    while True:
        deleted = input("Выберите какую звезду будем удалять: ")
        try:
            del star_dict[deleted]
            print("Звезда успешно удалена")
            break
        except KeyError:
            print("Такой звезды не существует. Попробуйте ещё раз")


def add_obj():
    if len(star_dict) + 1 < 12:
        print("Вы вошли в режим добавление нового небесного тела. "
              "Название звезды и созвездия не должно превышать 20 символов!")
        while True:
            name_star = input("Введите название звезды: ")
            if input(f"Звезда называется \"{name_star}\"? (д/н) ").lower() in ["д", "", "да"]:
                break
        while True:
            name_constellation = input("Введите название созвездия: ")
            if input(f"Звезда находится в созвездии \"{name_constellation}\"? (д/н) ").lower() in ["д", "", "да"]:
                break
        while True:
            try:
                distance = int(input("Введите расстояние в световых годах (округлите до целого числа): "))
                if input(f"От Солнца до {name_star} {distance} св. лет(года)? (д/н) ").lower() in ["д", "", "да"]:
                    break
            except ValueError:
                print("Данные не являются целым числом. Попробуйте ещё раз.")
        while True:
            try:
                weight = int(input("Введите массу в массах Солнца (округлите до целого числа): "))
                if input(f"Масса {name_star} {weight} масс Солнца? (д/н) ").lower() in ["д", "", "да"]:
                    break
            except ValueError:
                print("Данные не являются целым числом. Попробуйте ещё раз.")
        star_dict[name_star] = Star(name_constellation, distance, weight)
        print(f"Создан новый объект:\nЗвезда: {name_star}\nСозвездие: {name_constellation}\n"
              f"Расстояние от Солнца (в св. годах): {distance}\nМасса (в массах Солнца): {weight}")
    else:
        print("Невозможно добавить новый объект!\nУдалите один объект, чтобы добавить новый.")


def close_console():
    """Закрытие программы"""
    exit(1)


def executing_the_command():
    try:
        commands = {"выход": close_console, "добавить": add_obj, "удалить": del_obj, "список": list_obj,
                    "сортировать": sort_obj, "фильтр": filter_obj, "перевод в парсеки": convert_obj}
        commands[command.split(" ")[0]]()
    except KeyError:
        print("Такой команды не существует!")


if __name__ == "__main__":
    print("«Каталог звезд нашей галактики»\n\nСписок возможных команд:\nдобавить - добавление звезды\n"
          "удалить - удаление выбранной звезды\nсписок - вывод всех звезд в виде таблицы\n"
          "сортировать - сортировка звезд по выбранному параметру\n"
          "фильтр - вывод всех звезд, у которых масса не превосходит заданной величины\n"
          "перевод в парсеки - вывод расстояния от Солнца до звезд в парсеках\nвыход - выход из программы\n")
    while True:
        command = input("Введите команду: ")
        executing_the_command()
