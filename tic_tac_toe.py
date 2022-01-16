"""
    Project: Tic-Tac-Toe
    Author: Miguel I. Prot Garcia

    Tic-Tac-Toe is played according to the following rules.

    1) The game is played on a grid that is three squares by three squares.
    2) Player one uses x's. Player two uses o's.
    3) Players take turns putting their marks in empty squares.
    4) The first player to get three of their marks in a row (vertically, horizontally, or diagonally) is the winner.
    5) If all nine squares are full and neither player has three in a row, the game ends in a draw.
"""

def main():
    turn = who_is_playing("")
    grid = create_grid()
    win = False
    draw = False
    while not ( win or draw ):
        show_board_status(grid)
        ask_to_user(turn, grid)
        win = winner(grid)
        draw = is_draw(grid)
        turn = who_is_playing(turn)
        
    if win:
        print("Good game. Thanks for playing!")
    if draw:
        print("Looks like you both have the same level.")
        print("Good game. Thanks for playing!")
    
    pass

def ask_to_user(turn, grid):
    choise = int(input(f"{turn}'s turn to choose a square (1-9): "))
    index = choise - 1
    grid[index] = turn
    pass

def create_grid():
    grid = []
    for square_item in range(1,10):
        grid.append(square_item)
    return grid

def show_board_status(grid):
    for index, element in enumerate(grid):
        print(element, end=""),
        if (index == 0 or index == 1 
        or index == 3 or index == 4 
        or index == 6 or index == 7):
            print(' | ', end="")
        elif (index == 2 or index == 5 ):
            print('\n- + - + -')
        else: print()
    print()

def winner(board):
    if ( board[0] is board[1] is board[2] or board[0] is board[3] is board[6] or board[0] is board[4] is board[8] ):
        print(f"The winner is {board[0]}!!")
        return True
    elif ( board[3] is board[4] is board[5] ):
        print(f"The winner is {board[3]}!!")
        return True
    elif ( board[6] is board[7] is board[8] or board[2] is board[4] is board[6] ):
        print(f"The winner is {board[6]}!!")
        return True
    elif (board[1] is board[4] is board[7]):
        print(f"The winner is{board[0]}!!")
        return True
    elif (board[2] is board[5] is board[8]):
        print(f"The winner is{board[0]}!!")
        return True
    else:
        return False

def is_draw(grid):
    for index in range(9):
        if grid[index] != 'x' or grid[index] != 'o':
            return False
        else:
            return True

def who_is_playing(current_turn):
    if current_turn == 'x':
        return 'o'
    elif current_turn == 'o':
        return 'x'
    else:
        return 'x'

if __name__ == "__main__":
    main()