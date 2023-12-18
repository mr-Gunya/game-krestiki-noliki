# игра крестики - нолики
def greetings():
    print("-------------------")
    print("  Добро пожаловать ")
    print("      в игру       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")


def display_board():
    print()
    print("  | 0 | 1 | 2 |")
    print("---------------")
    for i in range(3):
        row = " | ".join(board[i])
        print(f"{i} | {row} |")
        print("---------------")


def make_move():
    while True:
        coordinates = input("Сделайте ход: ").split()
        if len(coordinates) != 2:
            print("Введите две координаты: ")
            continue
        x, y = coordinates
        if not (x.isdigit()) or not (y.isdigit()):
            print("Введите числа через пробел: ")
            continue
        x, y = int(x), int(y)
        if 0 <= x <= 2 and 0 <= y <= 2:
            if board[x][y] == " ":
                return x, y
            else:
                print("Ячейка уже занята! Попробуйте ещё раз: ")
        else:
            print("Координаты вне диапозона! Повторите попытку: ")


def check_win():
    # win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
    #             ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
    #             ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    # for cord in win_cord:
    #     symbols = []
    #     for c in cord:
    #         symbols.append(board[c[0]][c[1]])
    #     if symbols == ["X", "X", "X"]:
    #         print("Выиграл X!!!")
    #         return True
    #     if symbols == ["0", "0", "0"]:
    #         print("Выиграл 0!!!")
    #         return True
    # return False
    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(board[i][j])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        elif symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True

    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(board[j][i])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        elif symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True

    symbols = []
    for i in range(3):
        symbols.append(board[i][i])
    if symbols == ["X", "X", "X"]:
        print("Выиграл X!!!")
        return True
    elif symbols == ["0", "0", "0"]:
        print("Выиграл 0!!!")
        return True

    symbols = []
    for i in range(3):
        symbols.append(board[i][2 - i])
    if symbols == ["X", "X", "X"]:
        print("Выиграл X!!!")
        return True
    elif symbols == ["0", "0", "0"]:
        print("Выиграл 0!!!")
        return True
    return False


greetings()
board = [[" "] * 3 for i in range(3)]
num = 0
while True:
    num += 1

    display_board()
    if num % 2 == 1:
        print("Ходит крестик: ")
    else:
        print("Ходит нолик: ")

    x, y = make_move()
    if num % 2 == 1:
        board[x][y] = "X"
    else:
        board[x][y] = "0"

    if check_win():
        break

    if num == 9:
        print("Ничья!")
        break
