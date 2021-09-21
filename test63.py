# День рождение
# Демонстрирует именованные аргументы и значения параметров по умолчанию
# позиционные параметры

name = input("Введите имя: ")
age = int(input("Введиет возраст: "))


def birthday1(name, age):
    print("С Днем Рождения,", name, "!", "Вам сегодня исполнилось", age, ", не так ли?\n")


# пармаетры со значениями по умолчанию
def birthday2(name="Товарищ Иванов", age=1):
    print("С Днем Рождения,", name, "!", "Вам сегодня исполнилось", age, ", не так ли?\n")


# birthday1("Товарищ Иванов", 1)
# birthday1(1, "Товарищ Иванов")
# birthday1(name="Товарищ Иванов", age=1)
# birthday1(age=1, name="Товарищ Иванов")
birthday1(name, age)
# birthday2()
# birthday2(name="Катя")
# birthday2(age=12)
# birthday2(name="Катя", age=12)
# birthday2("Катя", 12)
input("\n\nClick Enter to leave.")