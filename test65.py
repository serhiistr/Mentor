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


def display_board(board):
    """Отображает игровую доску на экране"""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")


def legal_moves(board):
    """Создает список доступных ходов"""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    """Определяет победителя в игре"""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] !=EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None


def human_move(board, human):
    """Получает ход человек"""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Твой ход. Выбери одно из полей (0-8):", O, NUM_SQUARES)
        if move not in legal:
            print("\nСмешной человек! Это поле уже занято. Выбери другое.\n")
    print("Ладно...")
    return move


def computer_move(board, computer, human):
    """Делает ход за компьютерного противника."""
    # Создадим робочую копию доски, потому что функция будет менять некоторые значения в списке
    board = board[:]


    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("Я выберу поле номер", end=" ")

    for move in legal_moves(board):
        board[move] = computer
    # Если следующим ходом может победить компьютер, выберем этот ход
    if winner(board) == computer:
        print(move)
        return move
    # выполнив проверку, отменим внесенные изменения
    board[move] = EMPTY
    # Поскольку следующим ходом ни одна сторона не может победить.
    # выберем лучшее из доступных полей
    for move in legal_moves(board):
        print(move)
        return move




