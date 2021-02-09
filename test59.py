# Переводчик с гикского на русский
# Демонстрирует использование словарей

geek = {"404": "Не знать, не владеть информацией. От сообщения об ошибке 404 'Страница не найдена'.",
        "Googling": "'Гугление', поиск в Сети сведений о ком-либо.",
        "Keyboard Plague": "Мусор, который скапливается в клавиатуре компьютера.",
        "Link Rot": "Процесс устаревания ссылок на веб-страницах.",
        "Percussive Maintenance": "О ситуации, когда кто-либо бьет по корпусу неисправного"
                                  " элекронного прибора в надежде восстановить его работу",
        "Uninstalled": "Об увольнении кого-либо. Особенно популярно на рубеже 1990-2000-х годов."}

# print(geek["404"], end=" ")
#
# print(geek["Link Rot"])
#
# print(geek.get("Dancing Baloney", "Понятия не имею"))
# print(geek.get("Link Rot"))
# print(geek.get("Dancing Baloney"))

choice = None
while choice != "0":
        print(
                """
                Переводчик с гикского на русский
                0 - Выйти
                1 - Найти толкование ермина
                2 - Добавить термин
                3 - Изменить толкование
                4 - Удалить термин
                 """)
        choice = input("Your choice: ")
        print()
        # Выход
        if choice == "0":
                print("Good buy")

        # Поиск толкования
        elif choice == "2":
                term = input("Какой термин гикского языка вы хотите добавить: ")
                if term not in geek:
                        definition = input("Введите олкование: ")
                        geek[term] = definition
                        print("\nТермин", term, "добавлен в словарь.")
                else:
                        print("\nТакой термин уже есть! Попробуйте изменить его толкование")

