import os
import random

board = [' ' for _ in range(9)]

def print_board():
    row1 = '| {}                  \t\t        | {}          \t\t                  | {}            \t\t               |'.format(board[0], board[1], board[2])
    row2 = '| {}                  \t\t        | {}          \t\t                  | {}            \t\t               |'.format(board[3], board[4], board[5])
    row3 = '| {}                  \t\t        | {}          \t\t                  | {}            \t\t               |'.format(board[6], board[7], board[8])
     
    print()
    print("_________________________________________________________________________________________________________________________________")
    print(row1)
    print("_________________________________________________________________________________________________________________________________")
    print(row2)
    print("_________________________________________________________________________________________________________________________________")
    print(row3)
    print("_________________________________________________________________________________________________________________________________")
    print()

def check_win():
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return True
    return False

def check_draw():
    return ' ' not in board

def play_game():
    global board
    board = [' ' for _ in range(9)]
    opponent = input("Do you want to play with a human or a computer? (human/computer): ")
    if opponent == 'human':
        player1 = input("Enter Player 1's name: ")
        player2 = input("Enter Player 2's name: ")
        current_player = player1
    else:
        player1 = input("Enter your name: ")
        player2 = 'Computer'
        current_player = player1

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_board()
        if opponent == 'human':
            move = input("{}'s turn, enter your move (1-9): ".format(current_player))
        else:
            if current_player == player1:
                move = input("{}'s turn, enter your move (1-9): ".format(current_player))
            else:
                move = str(random.randint(1, 9))
                print("{}'s turn, move: {}".format(player2, move))
        if board[int(move) - 1] == ' ':
            board[int(move) - 1] = player1 if current_player == player1 else player2
            if check_win():
                os.system('cls' if os.name == 'nt' else 'clear')
                print_board()
                print("{} wins! Congratulations!".format(current_player))
                break
            elif check_draw():
                os.system('cls' if os.name == 'nt' else 'clear')
                print_board()
                print("It's a draw!")
                break
            current_player = player2 if current_player == player1 else player1
        else:
            print("Invalid move, try again.")

while True:
    play_game()
    choice = input("Do you want to play again? (yes/no): ")
    if choice.lower() != "yes":
        print("good bye")
        break
