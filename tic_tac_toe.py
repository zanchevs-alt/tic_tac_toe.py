def create_board():
    """Returns a new empty board"""
    return [" "] * 9

def print_board(board):
    """Print the board with grid formatting"""
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def get_move(current_player, board):
    """Ask the player to choose a spot and validate input"""
    while True:
        print(f" player: {current_player} ")
        move = int(input(" enter move (1-9): "))
        if 0 >= move or move >= 10:
            print("Please enter a number between 1 and 9.")
            continue
        move = int(move) - 1
        if board[move] == " ":
            return move
        else:
            print("That spot is invalid or already taken. Try again.")


def make_move(board, position, symbol):
    """Updates the board at the given position"""
    board[position] = symbol

def check_winner(board):
    """Returns True if a player has 3 in a row"""
    # Rows
    if (board[0] == board[1] == board[2] != " ") or \
       (board[3] == board[4] == board[5] != " ") or \
       (board[6] == board[7] == board[8] != " "):
        return True
    # Columns
    if (board[0] == board[3] == board[6] != " ") or \
       (board[1] == board[4] == board[7] != " ") or \
       (board[2] == board[5] == board[8] != " "):
        return True
    # Diagonals
    if (board[0] == board[4] == board[8] != " ") or \
       (board[2] == board[4] == board[6] != " "):
        return True
    return False

def is_tie(board):
    """Returns True if no spots left and no winner"""
    if " " in board:
        return False
    if check_winner(board):
        return False

    return True

def switch_player(current):
    """Switch between X and O"""
    if current == "X":
        return "O"
    else:
        return "X"

def play_game():
    """Runs the whole game loop"""
    board = create_board()
    current_player = "X"
    game_over = False

    print_board(board)

    while not game_over:
        move = get_move(current_player, board)
        make_move(board, move, current_player)
        print_board(board)

        if check_winner(board):
            print(f"Game Over! Player {current_player} wins!")
            game_over = True
        elif is_tie(board):
            print("It's a tie!")
            game_over = True
        else:
            current_player = switch_player(current_player)


play_game()