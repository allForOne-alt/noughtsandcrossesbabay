import json
import os.path
import random

random.seed()


def draw_board(board):
    """code to draw the board"""
    for i in range(3):
        print(f"{board[i][0]} | {board[i][1]} | {board[i][2]} ")
        if i < 2:
            print("---------------")
    print("\n")


def welcome(board):
    """
    prints the welcome message
    draw_board(board)
    """
    draw_board(board)


def initialise_board(board):
    """develop code to set all elements of the board to one space ' '"""

    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    return board


def get_player_move(board):
    """
    develop code to ask the user for the cell to put the X in,
    and return row and col
    """

    positions = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2),
    }

    while True:
        try:
            posi = int(input("Enter position (1-9) : "))
            if posi not in positions:
                # print("Invalid Position (1-9 only)")
                continue
            row, col = positions[posi]
            if board[row][col] != " ":
                continue
            return row, col
        except ValueError:
            print("Invalid input (1-9 only)")


def choose_computer_move(board):
    """
    develop code to let the computer chose a cell to put a nought in
    and return row and col
    """
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            return row, col


def check_for_win(board, mark):
    """
    develop code to check if either the player or the computer has won
    return True if someone won, False otherwise
    """
    # rows
    for i in range(3):
        if board[i][0] == mark and board[i][1] == mark and board[i][2] == mark:
            return True

    # cols
    for j in range(3):
        if board[0][j] == mark and board[1][j] == mark and board[2][j] == mark:
            return True

    # diagonals
    if board[0][0] == mark and board[1][1] == mark and board[2][2] == mark:
        return True
    if board[0][2] == mark and board[1][1] == mark and board[2][0] == mark:
        return True

    return False


def check_for_draw(board):
    """
    develop cope to check if all cells are occupied
    return True if it is, False otherwise
    """
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True


def play_game(board):
    board = initialise_board(board)
    draw_board(board)

    while True:
        # player
        print("Your Turn")
        row, col = get_player_move(board)
        board[row][col] = "x"
        draw_board(board)

        if check_for_win(board, "x"):
            print("YOU WON!!!")
            return 1

        if check_for_draw(board):
            print("DRAW!!")
            return 0

        # computer
        print("Computer's Turn")
        row, col = choose_computer_move(board)
        board[row][col] = "0"
        draw_board(board)

        if check_for_win(board, "0"):
            print("COMPUTER WON!!!")
            return -1

        if check_for_draw(board):
            print("DRAW!!")
            return 0


def menu():
    # get user input of either '1', '2', '3' or 'q'
    # 1 - Play the game
    # 2 - Save score in file 'leaderboard.txt'
    # 3 - Load and display the scores from the 'leaderboard.txt'
    # q - End the program

    while True:
        print("1 - Play the game")
        print("2 - Save score")
        print("3 - Load and display the scores")
        print("q - End the program")
        choice = input("Enter you choice : ").lower()

        if choice in ["1", "2", "3", "q"]:
            return choice
        else:
            print("Invalid choice, 1, 2, 3, or q to quit")


def load_scores():
    """
    develop code to load the leaderboard scores
    from the file 'leaderboard.txt'
    return the scores in a Python dictionary
    with the player names as key and the scores as values
    return the dictionary in leaders
    """
    leaders = {}
    if os.path.exists("leaderboard.txt"):
        try:
            with open("leaderboard.txt", "r") as file:
                leaders = json.load(file)
        except (IOError, json.JSONDecodeError):
            leaders = {}
    return leaders


def save_score(score, name=None):
    # develop code to ask the player for their name
    # and then save the current score to the file 'leaderboard.txt'
    if name is None:
        name = input("Enter you name : ")
    
    leaders = load_scores()

    if name in leaders:
        leaders[name] += score
    else:
        leaders[name] = score

    with open("leaderboard.txt", "w") as file:
        json.dump(leaders, file)

def display_leaderboard(leaders):
    """
    develop code to display the leaderboard scores
    passed in the Python dictionary parameter leader
    """

    if not leaders:
        print("There are no scores yet")
        return

    score_list = list(leaders.items())

    for i in range(len(score_list)):
        max_i = i  # assuming that i has the highest score
        for j in range(i + 1, len(score_list)):
            if score_list[j][1] > score_list[max_i][1]:
                max_i = j

        score_list[i], score_list[max_i] = score_list[max_i], score_list[i]

    print("-------------LEADER-BOARD----------------")
    for name, score in score_list:
        print(f"{name}: {score}")
    print()


