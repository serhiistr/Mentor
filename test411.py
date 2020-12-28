# Арсенал героя
# Демонсрирует создание кортежа
# создадим пустой кортеж

inventory = ()

# рассмртрим его как условие
if not inventory:
    print("Вы безоружны")

input("Click Enter to continue.")

# теперь создадим кортеж на экран
inventory = ("меч",
            "кольчуга",
            "щит",
            "целебное снадобье")

# выведем этот кортеж на экран
print("\nСодержимое кортежа")
print(inventory)

# выведем все элементы последовательно
print("\nИтак, в нашем арменале: ")
for item in inventory:
    print(item)

input("Click Enter to leave.")