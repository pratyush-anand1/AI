import random

def play_game(num_sticks,current_player):
    # current_player = 1
    while num_sticks > 0:
        print(f"\n{num_sticks} sticks left.")
        if current_player == 1:
            num = int(input("Player 1: How many sticks do you take? "))
        else:
            num = minimax(num_sticks, 2, -float('inf'), float('inf'))[1]
            print(f"Player 2: takes {num} sticks")
        if num < 1 or num > 3:
            print("Invalid number of sticks. You can only take 1-3 sticks.")
            continue
        elif num > num_sticks:
            print(f"You cannot take more than {num_sticks} sticks.")
            continue
        num_sticks -= num
        current_player = 3 - current_player
    print(f"\nPlayer {current_player} wins!")

def evaluate_game(num_sticks, current_player):
    if num_sticks == 1:
        return -1 if current_player == 1 else 1
    elif num_sticks == 2:
        return 1 if current_player == 1 else -1
    elif num_sticks == 3:
        return -1 if current_player == 1 else 1
    else:
        return 0

def minimax(num_sticks, current_depth, alpha, beta):
    if current_depth == 0 or num_sticks <= 0:
        return evaluate_game(num_sticks, 2), None
    
    best_value, best_move = -float('inf'), None
    for i in range(1, 4):
        if num_sticks - i < 0:
            break
        value = -minimax(num_sticks - i, current_depth - 1, -beta, -alpha)[0]
        if value > best_value:
            best_value, best_move = value, i
        alpha = max(alpha, value)
        if alpha >= beta:
            break
    
    return best_value, best_move

#main
num_sticks=int(input("Enter the total number of sticks: "))
print(f"There are {num_sticks} sticks in the pile.")
# current_player=random.randint(0,1)
print("TOSS TIME")
toss=int(input("Enter 0 or 1: "))
if toss==random.randint(0,1):
    print("Congrats! You won the toss...\n")
    play_game(num_sticks,1)
else:
    print("Oops! You lost the toss...\n")
    play_game(num_sticks,2)