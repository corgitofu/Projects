def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def play_game():
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

    current_player = "X"
    winner = None

    while not winner and not is_board_full(board):
        print_board(board)

        row = int(input("Enter the row (1-3): "))
        col = int(input("Enter the column (1-3): "))

        if board[row-1][col-1] == " ":
            board[row-1][col-1] = current_player
            winner = check_winner(board)
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Your move was invalid, please try again.")

    print_board(board)

    if winner:
        print("Player", winner,  "wins!")
    else:
        print("It's a tie!")

play_game()
