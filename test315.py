# Эксклюзивная сеть
# Демонстрирует составные условия и логические операторы
print("\tЭксклюзивная компьюторная сеть")
print("\tТолько для зарегиcтрированных пользователей!\n")
security = 0
userame = ""

while not userame:
    userame = input("Логин: ")
password = ""

while not password:
    password = input("пароль: ")

if userame == "M.Dawson" and password == "secret":
    print("Привет, Майк.")
    security = 5
elif userame == "S.Meier" and password == "civilization":
    print("Здравствуй, Сид.")
    security = 3
elif userame == "S.Miyamoto" and password == "mariobros":
    print("Доброго времени суток, Сигеру.")
    security = 3
elif userame == "W.Wright" and password == "thesims":
    print("Как дела, Уилл?")
    security = 3
elif userame == "guest" or password == "guest":
    print("Доброго времени суток, Сигеру.")
    security = 1
else:
    print("Войти в системму не удалось. Должны быть, вы не очень-то эксклюзивный "
          "гражданин.\n")
input("\n\nНажмите Enter, чтобы выйти.")