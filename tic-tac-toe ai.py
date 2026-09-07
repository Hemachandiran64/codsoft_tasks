import math

board = [" "] * 9

def display():
    print()
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("--+---+--")

def winner():
    combinations = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]

    for a, b, c in combinations:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    if " " not in board:
        return "Draw"

    return None

def minimax(is_maximizing):
    result = winner()

    if result == "O":
        return 1
    if result == "X":
        return -1
    if result == "Draw":
        return 0

    if is_maximizing:
        best = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best = max(best, score)

        return best

    else:
        best = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best = min(best, score)

        return best

def best_move():
    best_score = -math.inf
    move = 0

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move

print("Tic-Tac-Toe")
print("You = X, Computer = O")

while True:
    display()

    player = int(input("Enter position (1-9): ")) - 1

    if board[player] != " ":
        print("Position already occupied!")
        continue

    board[player] = "X"

    if winner():
        break

    computer = best_move()
    board[computer] = "O"

    if winner():
        break

display()

result = winner()

if result == "X":
    print("You Win!")
elif result == "O":
    print("Computer Wins!")
else:
    print("It's a Draw!")