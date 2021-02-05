# Рекорды 2.0
# Демонстрирует вложеные последовательности
scores = []
choice = None
# name, score = ("Иван Иванович", 175)

while choice != "0":
    print("""
    Рекорды
    0 - Выйти
    1 - Показать рекорды
    2 - Добавить рекорд
    """)
    choice = input("You choice: ")
    print()

    # exit
    if choice == "0":
        print("Good bay")

    # вывод таблицы рекордов
    elif choice == "1":
        print("Рекорды\n")
        print("Имя\tРезультат")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)

    # add a score
    elif choice == "2":
        name = input("Впишите имя игрока: ")
        score = int(input("Впишите его результат: "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]          # В списке остается только пять рекордов

    # непонятный пользовательский ввод
    else:
        print("Извините, в меню нет пункта ", choice)

input("Click Enter to leave")