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
    grid = create_grid()
    show_board_status(grid)
    win = winner(grid)
    print(win)
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
    pass 

def winner(board):
    if (
        #horizontal
        board[0] == board[1] == board[2] or
        board[3] is board[4] is board[5] or
        board[6] is board[7] is board[8] or
        #vertical
        board[0] is board[3] is board[6] or
        board[0] is board[1] is board[2] or
        board[0] is board[1] is board[2] or
        #diagonal
        board[0] is board[1] is board[2] or
        board[0] is board[1] is board[2]
        ):
        return True
    else:
        return False
    pass

if __name__ == "__main__":
    main()