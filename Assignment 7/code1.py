#Tic tac toe using alpha beta pruning

BOARD_SIZE = 3
PLAYER_X = 'X'
PLAYER_O = 'O'

# Evaluation function for Tic-Tac-Toe board


def evaluate(board):
    for i in range(BOARD_SIZE):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == PLAYER_X:
                return 10
            elif board[i][0] == PLAYER_O:
                return -10
        # Check columns
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == PLAYER_X:
                return 10
            elif board[0][i] == PLAYER_O:
                return -10
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == PLAYER_X:
            return 10
        elif board[0][0] == PLAYER_O:
            return -10
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == PLAYER_X:
            return 10
        elif board[0][2] == PLAYER_O:
            return -10
    # No winner yet
    return 0

# Alpha-Beta pruning algorithm for Tic-Tac-Toe


def alpha_beta(board, alpha, beta, maximizing_player):
    # Check if game is over
    score = evaluate(board)
    if score != 0:
        return score
    # Check if board is full
    if all(board[i][j] != ' ' for i in range(BOARD_SIZE) for j in range(BOARD_SIZE)):
        return 0
    # Maximize score for Player X
    if maximizing_player:
        max_score = -1000
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board[i][j] == ' ':
                    board[i][j] = PLAYER_X
                    max_score = max(max_score, alpha_beta(
                        board, alpha, beta, False))
                    board[i][j] = ' '
                    alpha = max(alpha, max_score)
                    if alpha >= beta:
                        break
            if alpha >= beta:
                break
        return max_score
    # Minimize score for Player O
    else:
        min_score = 1000
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board[i][j] == ' ':
                    board[i][j] = PLAYER_O
                    min_score = min(min_score, alpha_beta(
                        board, alpha, beta, True))
                    board[i][j] = ' '
                    beta = min(beta, min_score)
                    if alpha >= beta:
                        break
            if alpha >= beta:
                break
        return min_score

# Main function to play Tic-Tac-Toe with alpha-beta pruning


def play_tic_tac_toe():
    # Initialize empty board
    board = [[' ' for j in range(BOARD_SIZE)] for i in range(BOARD_SIZE)]
# Play game
    while True:
        # Player X's turn
        print("Player X's turn")
        print_board(board)
        while True:
            i = int(input("Enter row: "))
            j = int(input("Enter column: "))
            if board[i][j] == ' ':
                board[i][j] = PLAYER_X
                break
            else:
                print("That spot is already taken!")
        # Check if game is over
        score = evaluate(board)
        if score != 0:
            print("Player X wins!" if score > 0 else "Player O wins!")
            break
        # Check if board is full
        if all(board[i][j] != ' ' for i in range(BOARD_SIZE) for j in range(BOARD_SIZE)):
            print("It's a tie!")
            break
        # Player O's turn
        print("Player O's turn")
        print_board(board)
        # Use alpha-beta pruning to find best move for Player O
        min_score = 1000
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board[i][j] == ' ':
                    board[i][j] = PLAYER_O
                    score = alpha_beta(board, -1000, 1000, True)
                    board[i][j] = ' '
                    if score < min_score:
                        min_score = score
                        best_move = (i, j)
        i, j = best_move
        board[i][j] = PLAYER_O
        # Check if game is over
        score = evaluate(board)
        if score != 0:
            print("Player X wins!" if score > 0 else "Player O wins!")
            break
        # Check if board is full
        if all(board[i][j] != ' ' for i in range(BOARD_SIZE) for j in range(BOARD_SIZE)):
            print("It's a tie!")
            break


def print_board(board):
    print('-------------')
    for i in range(BOARD_SIZE):
        print('|', end='')
        for j in range(BOARD_SIZE):
            print(' ' + board[i][j] + ' |', end='')
        print()
        print('-------------')


play_tic_tac_toe()