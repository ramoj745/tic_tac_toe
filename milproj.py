import random

def display_board(board):

    grid = [
        [board[7], board[8], board[9]],
        [board[4], board[5], board[6]],
        [board[1], board[2], board[3]]
    ]
    for row in grid:
        print(row)

def player_input():
    placeholder = ''
    while not (placeholder == 'X' or placeholder == 'O'):
        placeholder = input("X or O?: ").upper()

    player1 = placeholder

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
        player1 = 'O'

    return (player1, player2)

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark): #boolean

    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark))

def choose_first():
    odds = random.randint(0,1)
    if odds == 0:
        print("Player 1 goes first")
        return odds
    else:
        print("Player 2 goes first")
        return odds


def space_check(board, position): #true if there's space

    for space in board[position]:
        if ' ' in space:
            return True

    return False

def full_board_check(board): #true if there's no more space

    for space in board:
        if space == ' ':
            return False

    return True

def player_choice(board):

    check = False
    while not check:

        position = int(input("Choose position (1-9): "))
        space_check(board, position)
        if space_check(board, position) == True:
            return position
        else:
            print("Choose another position. That position is taken.")

def replay():

    again = input("Do you want to play again? Yes or No: ")
    if again == "Yes":
        return True
    else:
        pass

def player_1():
        display_board(test_board)
        posi1 = player_choice(test_board)
        print("\n" * 100)
        if space_check(test_board, posi1):
            place_marker(test_board, player1, posi1)

def player_2():
        display_board(test_board)
        posi2 = player_choice(test_board)
        print("\n" * 100)
        if space_check(test_board, posi2):
            place_marker(test_board, player2, posi2)


def player1goesfirst():
    while True:
        player_1()
        player1win = win_check(test_board, player1)
        if player1win:
            print("Player 1 has won the game!")
            return (True, False)
        if full_board_check(test_board):
            print("Full board! Exiting...")
            break

        player_2()
        player2win = win_check(test_board, player2)
        if player2win:
            print("Player 2 has won the game!")
            return (False, True)
        if full_board_check(test_board):
            print("Full board! Exiting...")
            break


def player2goesfirst():
    while True:
        player_2()
        player2won = win_check(test_board, player2)
        if player2won:
            print("Player 2 has won the game!")
            return (False, True)

        player_1()
        player1won = win_check(test_board, player1)
        if player1won:
            print("Player 1 has won the game!")
            return (True, False)


sample_test_board = ['#','O','O','X','X','O','X','O','X',' ']

print('Welcome to Tic Tac Toe!')
player1, player2 = player_input()
play1_play2 = choose_first()

while True:
    test_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ask = input("Are you ready to play? Yes or No: ")
    if ask == 'Yes':
        print("\n" * 100)
        if play1_play2 == 0:
            player1win, player2win = player1goesfirst()
            if player1win:
                if replay():
                    continue
                else:
                    break
            elif player2win:
                if replay():
                    continue
                else:
                    break
        elif play1_play2 == 1:
            player1won, player2won = player2goesfirst()
            if player1won:
                if replay():
                    continue
                else:
                    break
            elif player2won:
                if replay():
                    continue
                else:
                    break