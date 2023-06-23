import copy

board = [[' ' for _ in range(3)] for _ in range(3)]

def print_board():
    for row in board:
        print(row)

def check_win(board):
    # check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]
    # check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[2][0] == board[1][1] == board[0][2] and board[2][0] != ' ':
        return board[2][0]
    return None

def minimax(board, player):
    winner = check_win(board)
    if winner:
        if winner == 'X':
            return -1
        else:
            return 1
    if not any(' ' in row for row in board):
        return 0

    best_score = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = player
                score = minimax(board, 'O' if player == 'X' else 'X')
                board[row][col] = ' '
                if player == 'X':
                    if best_score is None or score > best_score:
                        best_score = score
                else:
                    if best_score is None or score < best_score:
                        best_score = score
    return best_score

def get_ai_move(board):
    best_score = None
    move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'X'
                score = minimax(board, 'O')
                board[row][col] = ' '
                if best_score is None or score > best_score:
                    best_score = score
                    move = (row, col)
    return move

print_board()
while True:
    move = input("Your move (row col): ").split()
    row = int(move[0])
    col = int(move[1])
    if board[row][col] != ' ':
        print("Invalid move, try again")
        continue
    board[row][col] = 'O'
    print_board()
    winner = check_win(board)
    if winner:
        print(winner, "wins!")
        break
    if not any(' ' in row for row in board):
        print("Tie!")
        break
    