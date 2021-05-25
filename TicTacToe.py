# --------------- GLOBAL VARIABLES ------------------ #
# Game board
board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

# Boolean for if game is still going
game_ongoing = True

# If tie then no winner
winner = None

# Player X goes first
current_player = "X"

# --------------------------------------------------- #

# Creating a game board
def print_board():
    # Printing row 1
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("------------")
    # Printing row 2
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("------------")
    # Printing row 3
    print(" " + board[6] + " | " + board[7] + " | " + board[8])

def start_game():
    # Display initial board
    print_board()

    while game_ongoing:
        # Handle turn of current player
        handle_turn(current_player)
        # Check if game is over
        check_game_over()
        # Switch to the other player
        switch_player()

    # Game is over
    if winner == "X" or winner == "O":
        print("Player " + winner + " won!")
    elif winner == None:
        print("Player X and O have tied!")

def handle_turn(player):
    # Get player's input
    print("Player " + player + "'s turn.")

    position = input("Make your move (Choose a position from 1-9): ")

    valid_input = False
    while not valid_input:
        # If the entered position is not from 1-9
        # Ask player for input until it is a valid input
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a position from 1-9: ")

        # Convert string position into int and correct to index 0
        position = int(position) - 1

        # If the position is taken, try again
        if board[position] == " ":
            valid_input = True
        else:
            print("Position is taken. Choose a different position.")

    board[position] = player
    print_board()

# Criteria for game ending
def check_game_over():
    # Checking if there's a winner
    check_for_winner()
    # Checking if there's a tie between players
    check_for_tie()

def check_for_winner():
    # Declaring global variable
    global winner
    # Checking rows
    row_filled = check_rows()
    # Checking columns
    column_filled = check_columns()
    # Checking diagonals
    diagonal_filled = check_diagonals()

    if row_filled:
        # There is a winner
        winner = row_filled
    elif column_filled:
        # There is a winner
        winner = column_filled
    elif diagonal_filled:
        # There is a winner
        winner = diagonal_filled
    else:
        # There is no winner
        # tied game
        winner = None
    return

def check_rows():
    # Declaring global variable
    global game_ongoing

    # If row 1 all has same variable and is not empty
    check_row_1 = board[0] == board[1] == board[2] != " "
    # If row 2 all has same variable and is not empty
    check_row_2 = board[3] == board[4] == board[5] != " "
    # If row 3 all has same variable and is not empty
    check_row_3 = board[6] == board[7] == board[8] != " "

    # If any row has the same variable, there is a winner
    if check_row_1 or check_row_2 or check_row_3:
        game_ongoing = False
    if check_row_1:
        return board[0]
    elif check_row_2:
        return board[3]
    elif check_row_3:
        return board[6]
    return

def check_columns():
    # Declaring global variable
    global game_ongoing

    # If col 1 all has same variable and is not empty
    check_col_1 = board[0] == board[3] == board[6] != " "
    # If col 2 all has same variable and is not empty
    check_col_2 = board[1] == board[4] == board[7] != " "
    # If col 3 all has same variable and is not empty
    check_col_3 = board[2] == board[5] == board[8] != " "

    # If any row has the same variable, there is a winner
    if check_col_1 or check_col_2 or check_col_3:
        game_ongoing = False
    if check_col_1:
        return board[0]
    elif check_col_2:
        return board[1]
    elif check_col_3:
        return board[2]
    return

def check_diagonals():
    # Declaring global variable
    global game_ongoing

    # If diagonal 1 all has same variable and is not empty
    check_diag_1 = board[0] == board[4] == board[8] != " "
    # If diagonal 2 all has same variable and is not empty
    check_diag_2 = board[6] == board[4] == board[2] != " "


    # If any row has the same variable, there is a winner
    if check_diag_1 or check_diag_2:
        game_ongoing = False
    if check_diag_1:
        return board[0]
    elif check_diag_2:
        return board[6]
    return

def check_for_tie():
    # Declaring global variable
    global game_ongoing
    if " " not in board:
        game_ongoing = False
    return

# Switch between X player and O player
def switch_player():
    # Declaring global variable
    global current_player
    # If current player is X, change to O player
    if current_player == "X":
        current_player = "O"
    # If current player is O, change to X player
    elif current_player == "O":
        current_player = "X"
    return

# Run the game
start_game()
