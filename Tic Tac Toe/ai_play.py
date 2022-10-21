import random

board_ = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

player_ = ["X", "O"]
ai_ = None
human = None
current = None
error = False
count = 0


def board():
    print("\n")
    for i in range(len(board_)):
        for j in range(0, 3):
            print(board_[i][j] + "\t", end="")
        print("\n")


def turn(row, column):
    global error
    if row <= 3 and column <= 3 and row >= 0 and column >= 0:
        if board_[row][column] == '-':
            board_[row][column] = current
        else:
            error = True
            print("this one is fill up please choose another")
    else:
        error = True
        print("Please enter number between 1 to 3")


def select_p(player=None):
    global human, player_, current, ai_
    if player is None:
        human = player_[random.randint(0, 1)]
        current = human
        if player_[player_.index(human)] == 'X':
            ai_ = 'O'
        else:
            ai_ = 'X'
        return current
    else:
        if player == human:
            current = ai_
        else:
            current = human
        return current


def ai_turn():
    global current
    final_move = minimax(board_)
    board_[final_move[0]][final_move[1]] = current


def minimax(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                board[i][j] = ai_
                score = check_winner(board)
                board[i][j] = '-'
                if score == ai_:
                    return [i, j]

    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                board[i][j] = human
                score = check_winner(board)
                board[i][j] = '-'

                if score == human:
                    return [i, j]

    if board[1][1] == '-':
        return [1, 1]

    # corner check
    cornerentry = [[0, 0], [0, 2], [2, 0], [2, 2]]
    data = random.randint(0, 3)

    if board[cornerentry[data][0]][cornerentry[data][1]] == '-':
        return [cornerentry[data][0], cornerentry[data][1]]

    otherdata = [[0, 1], [1, 0], [1, 2], [2, 1]]
    datas = random.randint(0, 3)

    if board[otherdata[datas][0]][otherdata[datas][1]] == '-':
        return [otherdata[datas][0], otherdata[datas][1]]


def check_winner(board):
    # check horizontal
    if board[0][0] == board[0][1] == board[0][2] != '-':
        return ai_ if board[0][0] == ai_ else human

    if board[1][0] == board[1][1] == board[1][2] != '-':
        return ai_ if board[1][0] == ai_ else human

    if board[2][0] == board[2][1] == board[2][2] != '-':
        return ai_ if board[2][0] == ai_ else human

    # check vertical
    if board[0][0] == board[1][0] == board[2][0] != '-':
        return ai_ if board[0][0] == ai_ else human

    if board[0][1] == board[1][1] == board[2][1] != '-':
        return ai_ if board[0][1] == ai_ else human

    if board[0][2] == board[1][2] == board[2][2] != '-':
        return ai_ if board[0][2] == ai_ else human

    # check for cross
    if board[0][0] == board[1][1] == board[2][2] != '-':
        return ai_ if board[0][0] == ai_ else human

    if board[0][2] == board[1][1] == board[2][0] != '-':
        return ai_ if board[0][2] == ai_ else human

    if count == 0 and current is not None:
        return 'tie'


def play_game():
    while True:
        board()
        global error, count
        fist = board_[0].count('-')
        sec = board_[1].count('-')
        thir = board_[2].count('-')
        count = fist + sec + thir

        if error == False:
            select_p(current)
        else:
            error = False

        try:
            if current == ai_:
                ai_turn()
            else:
                row = (int(input("Enter row in between [1-3] : ")) - 1)
                column = (int(input("Enter column in between [1-3] : ")) - 1)
                turn(row, column)
        except Exception as e:
            error = True
            print("You can enter number between 1 to 3 and only enter numbers.", e)

        rs = check_winner(board_)

        if rs == ai_:
            board()
            print(f"{current} is won the game")
            break
        elif rs == human:
            board()
            print(f"{current} is won the game")
            break
        elif rs == 'tie':
            board()
            print(f"Tie between both 'X' and 'O' player")
            break
        else:
            continue


play_game()
