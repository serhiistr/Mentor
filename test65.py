# Крестики-нолики
# Компьютер играет в крестики нолики против пользователя
# голобальные константы

X = "X"
O = "O"

EMPTY = ""
TIE = "Ничья"
NUM_SQUARES = 9

def display_instruct():
    """Выводит на экран инструкцию для игрока"""
    print("""
    Добро пожаловать на ринг грандиознейших интелектуальных состязаний всех времен.
    Твой мозг и мой процессор сойдутся в схватке за доской игры "КРЕСТИКИ-НОЛИКИ".
    Чтобы сделать ход, введи число от 0 до 8. Числа однозначно соответствуют полям доски - так, как показано ниже:
    
    0|1|2
    -----
    3|4|5
    -----
    6|7|8
    
    Приготовься к бою, жалкий белковатый человечишка. Вот-вот начнентся решающее сражение.\n
    
    """)


def ask_yes_no(question):
    """Задает вопрос с ответом 'ДА' или 'НЕТ'."""
    responce = None
    while responce not in ("y", "n"):
        responce = input(question).lower()
    return responce


def ask_number(question, low, high):
    """Просит ввести число из диапазона."""
    responce = None
    while responce not in range(low, high):
        responce = int(input(question))
    return responce


def pieces():
    """Определяет принадлежность первого хода"""
    go_first = ask_yes_no("Хочешь оставить з собой первый ход? (y/n): ")
    if go_first == "y":
        print("\nНу что ж, даю тебе фору: играй крестиками.")
        human = X
        computer = O
    else:
        print("\nТвоя удаль тебя погубит... Буду начинать Я.")
        human = O
        computer = X
    return computer, human


def new_board():
    """Создает новую игровую доску."""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


