# Только согласные
# Демонтсрирует, как создать новые строки из исходных с помощью цикла for

message = input("введите текст: ")
new_massege = ""
VOWELS = "йуеаыоэяию"
print()

for letter in message:
    if letter.lower() not in VOWELS:
        new_massege += letter
    print("Создана новая строка: ", new_massege)

print("\nВот ваш текст с изъятыми гласными буквами: ", new_massege)

input("\nClick Enter to leave")