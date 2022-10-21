import random

board_ = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

player_ = ["X", "O"]
active = None
win = False
tie = False
count = 0


def board():
    print("\n")
    for i in range(len(board_)):
        for j in range(0, 3):
            print(board_[i][j] + "\t", end="")
        print("\n")


def turn():
    try:
        row = (int(input("Enter row in between [1-3] : ")) - 1)
        column = (int(input("Enter column in between [1-3] : ")) - 1)

        if 0 < row <= 3 and 0 < column <= 3:
            pass
        else:
            print("\nPlease Enter Number In 1-3")
            row = (int(input("Enter row in between [1-3] : ")) - 1)
            column = (int(input("Enter column in between [1-3] : ")) - 1)
    except Exception as e:
        print("You can enter number between 1 to 3 and only enter numbers.")

    if active is None:
        if board_[row][column] == '-':
            board_[row][column] = select_p()
        else:
            print("this one is fill up please choose another")
    else:
        if board_[row][column] == '-':
            board_[row][column] = select_p(active)
        else:
            print("this one is fill up please choose another")


def select_p(player=None):
    if player is None:
        global active, player_
        active = player_[random.randint(0, 1)]
        return active
    else:
        c_index = player_.index(player)
        if c_index == 0:
            active = 'O'
        else:
            active = 'X'
        return active


def check_winner():
    # check horizontal
    global tie, count, win
    if board_[0][0] == board_[0][1] == board_[0][2] != '-':
        win = True
        print(f"{active} is won the game")

    if board_[1][0] == board_[1][1] == board_[1][2] != '-':
        win = True
        print(f"{active} is won the game")

    if board_[2][0] == board_[2][1] == board_[2][2] != '-':
        win = True
        print(f"{active} is won the game")

    # check vertical
    if board_[0][0] == board_[1][0] == board_[2][0] != '-':
        win = True
        print(f"{active} is won the game")

    if board_[0][1] == board_[1][1] == board_[2][1] != '-':
        win = True
        print(f"{active} is won the game")

    if board_[0][2] == board_[1][2] == board_[2][2] != '-':
        win = True
        print(f"{active} is won the game")

    # check for cross
    if board_[0][0] == board_[1][1] == board_[2][2] != '-':
        win = True
        print(f"{active} is won the game")

    if board_[0][2] == board_[1][1] == board_[2][0] != '-':
        win = True
        print(f"{active} is won the game")

    # check out for tie
    if count == 0 and active is not None:
        tie = True
        print(f"Tie between both 'X' and 'O' player")


def play_game():
    while True:
        board()

        global count
        fist = board_[0].count('-')
        sec = board_[1].count('-')
        thir = board_[2].count('-')
        count = fist + sec + thir

        turn()

        check_winner()

        if win is True:
            board()
            break

        if tie is True:
            board()
            break


play_game()
