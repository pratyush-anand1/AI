import random

def game_of_sticks(n_sticks):
    """
    Play the Game of Sticks with alpha-beta pruning algorithm.

    Parameters:
    - n_sticks: the number of sticks in the pile

    Returns:
    - True if the first player wins, False if the second player wins
    """

    def alpha_beta(state, alpha, beta, player):
        """
        Perform alpha-beta pruning to determine the best move for a given player.

        Parameters:
        - state: the current state of the game, represented as a tuple (n_sticks, player)
        - alpha: the best value for the maximizing player so far
        - beta: the best value for the minimizing player so far
        - player: the player whose turn it is to make a move

        Returns:
        - the best value for the given player
        """

        n_sticks, current_player = state

        # If there are no sticks left, the current player loses
        if n_sticks == 0:
            return -1 if current_player == 1 else 1

        # If it's the first player's turn, maximize the value
        if player == 1:
            best_value = float('-inf')
            for i in range(1, 4):
                if n_sticks >= i:
                    new_state = (n_sticks - i, 2)
                    value = alpha_beta(new_state, alpha, beta, 2)
                    best_value = max(best_value, value)
                    alpha = max(alpha, best_value)
                    if beta <= alpha:
                        break
            return best_value

        # If it's the second player's turn, minimize the value
        else:
            best_value = float('inf')
            for i in range(1, 4):
                if n_sticks >= i:
                    new_state = (n_sticks - i, 1)
                    value = alpha_beta(new_state, alpha, beta, 1)
                    best_value = min(best_value, value)
                    beta = min(beta, best_value)
                    if beta <= alpha:
                        break
            return best_value

    # Randomly decide which player goes first
    current_player = random.choice([1, 2])

    while n_sticks > 0:
        print("Number of sticks left in the pile: ", n_sticks)

        if current_player == 1:
            # Human player's turn
            n_removed = int(input("How many sticks do you want to remove? "))
            if n_removed < 1 or n_removed > min(n_sticks, 3):
                print("Invalid move. You must remove between 1 and", min(n_sticks, 3), "sticks.")
                continue
        else:
            # AI player's turn
            print("AI player is thinking...")
            best_value = float('-inf')
            best_move = None
            for i in range(1, 4):
                if n_sticks >= i:
                    new_state = (n_sticks - i, 1)
                    value = alpha_beta(new_state, float('-inf'), float('inf'), 1)
                    if value > best_value:
                        best_value = value
                        best_move = i
            n_removed = best_move
            print("AI player removes", n_removed, "sticks.")

        # Update the state of the game
        n_sticks -= n_removed
        current_player = 3 - current_player

    # The current player loses
    winner = 3 - current_player
    
    # The game is over, declare the winner
    print("Number of sticks left in the pile: 0")
    print("Game over. ", end="")
    if winner == 1:
        print("AI palyer wins!")
        return True
    else:
        print("You win!")
        return False

# Play the game
game_of_sticks(21)