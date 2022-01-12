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
    pass

def create_grid():
    grid = []
    for square_item in range(1,10):
        grid.append(square_item)
    return grid

def show_board_status(grid):
    for element in grid:
        print(element, end=""),
        if (element == 1 or element == 2 
        or element == 4 or element == 5 
        or element == 7 or element == 8):
            print(' | ', end="")
        elif (element == 3 or element == 6 ):
            print('\n- + - + -')
        else: print()
    pass 

if __name__ == "__main__":
    main()