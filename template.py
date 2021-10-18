# word = "TEMP"
#
# for i in range(-1, -len(word)-1, -1):
#     print(word[i])


# def main():
#     print("Hello world")
#
#
# main()
#
# print("OK")

EMPTY = " "
NUM_SQUARES = 9


def new_board():
    """Создает новую игровую доску."""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


board = new_board()


def display_board(board):
    """Отображает игровую доску на экране"""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")


display_board(board)



