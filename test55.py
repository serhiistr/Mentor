# Арсенал героя 3.0
# Демонстрирует работу со списками
# Создадим список с несколькими элементами и выведем его с помощью
# цикла for

inventory = ["меч", "кольчуга", "щит", "целебное снадобье"]

print("\nИтак в Вашем арсенале: ")

for item in inventory:
    print(item)

input("\nClick Enter to continue. ")

# Найдем длину списка
print("Сейчас в вашем распоряжении ", len(inventory), " предметов.")

input("\nClick Enter to continue.")

# проверка на принадлежность списку с помощью in
if "целебное снадобье" in inventory:
    print("Вы еще поживете и повоюете.")

# Вывод одного элемента с определенным индексом
index = int(input("\nВведите индекс одного из предметов арсенала: "))
print("Под индексом ", index, "в арсенале находится: ", inventory[index])

# отобразим срез
start = int(input("\nВведите начальный индекс среза: "))
finish = int(input("\nВведите конечный индекс среза: "))
print("Срез inventory[", start, ":", finish, "] - это", end=" ")
print(inventory[start:finish])
input("\nClick Enter to continue.")

# сцепление списков
chest = ["золото", "драгоценные камни"]
print("Вы нашли ларец. Вот что в нем есть: ")
print(chest)
print("Вы приобщили содержимое ларца к своему арсеналу.")
inventory = inventory + chest
print("Теперь в вашем распоряжении: ")
print(inventory)
input("Click Enter to continue")

# присваиваем значение элементу по индексу.
# Ловушка, если прописать какое либо значение элементу, которого ранее не существовало,
# вызовет ошибку
print("Вы обменяли меч на арбалет.")
inventory[0] = "арбалет"
print("Теперь ваш арсенал содержит следующие предметы: ")
print(inventory)
input("Click Enter to continue")

# приписываем значение элементам по срезу индексов
print("За золото и драгоценные камни Вы купили магический кристал, способный предсказать будущее.")
inventory[4:6] = ["магический кристалл"]
print("Теперь в вашем распоряжении: ")
print(inventory)
input("Click Enter to continue")

# удаляем элемент
print("В тяжелом бою был раздроблен Ваш щит.")
del inventory[2]
print("Во что осталось в арсенале: ")
print(inventory)
input("Click Enter to continue")

# удаляем срез
print("Воры лишили Вас арбалета и кольчуги.")
del inventory[:2]
print("Во что осталось в арсенале: ")
print(inventory)
input("Click Enter to continue")
