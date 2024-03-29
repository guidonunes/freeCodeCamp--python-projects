class Board:
    #instantiate object to a customized state
    def __init__(self, board):
        self.board = board
        
    def __str__(self):
    #create the borders of the board(upper, middle and lower lines)
        upper_lines = f'\n╔═══{"╤═══"*2}{"╦═══"}{"╤═══"*2}{"╦═══"}{"╤═══"*2}╗\n'
        middle_lines = f'╟───{"┼───"*2}{"╫───"}{"┼───"*2}{"╫───"}{"┼───"*2}╢\n' 
        lower_lines = f'╚═══{"╧═══"*2}{"╩═══"}{"╧═══"*2}{"╩═══"}{"╧═══"*2}╝\n'
        board_string = upper_lines
    #use enumeration to get both index and line of each row
        for index, line in enumerate(self.board):
            row_list = []
    #create the three lists of equal length representing the line segment of each 3x3 square
            for square_no, part in enumerate([line[:3], line[3:6], line[6:]], start=1):
                row_square = '|'.join(str(item) for item in part)
                row_list.extend(row_square)
    #check if the current segment(square_no) is not the last one
                if square_no != 3:
                    row_list.append('║')
            row = f'║ {" ".join(row_list)} ║\n'
            row_empty = row.replace('0', ' ')
            board_string += row_empty
    #handle the last row. The last row of the sudoku board has an index of 8         
            if index < 8:
                if index % 3 == 2:
                    board_string += f'╠═══{"╪═══"*2}{"╬═══"}{"╪═══"*2}{"╬═══"}{"╪═══"*2}╣\n'
                else:   
                    board_string += middle_lines
            else:
                board_string += lower_lines
    #return string containing the complete visual representation of the sudoku board
            return board_string
    
    def find_empty_cell(self):
        for row, contents in enumerate(self.board):
            try:
                col = contents.index(0)
                return row, col
            except ValueError:
                pass
                
        return None   
    
    #check if a given number can be inserted into a specified row
    def valid_in_row(self, row, num):
        return num not in self.board[row]
    
    #check if a given number can be inserted into a specified column
    def valid_in_col(self, col, num):
        return all(
        self.board[row][col] != num
        for row in range(9)
        )
    #check if a given number can be inserted in the 3x3 square
    def valid_in_square(self, row, col, num):
        row_start = (row//3) * 3
        col_start = (col//3) * 3
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
    #check if the specified number is already present in the current cell
                if self.board[row_no][col_no] == num:
                    return False
        return True
    
    def is_valid(self, empty, num):
        row, col = empty
    #check if the number is valid for insertion in the specified row/column/square  
        valid_in_row = self.valid_in_row(row, num)
        valid_in_col = self.valid_in_col(col, num)
        valid_in_square = self.valid_in_square(row, col, num)
    #Verifies if all function calls return True
        return all([valid_in_row, valid_in_col, valid_in_square])
    
    def solver(self):
        if (next_empty := self.find_empty_cell()) is None:
            return True
        else:
            for guess in range(1, 10):
        #checks if the number is a valid choice for the current empty cell
                if self.is_valid(next_empty, guess):
                    row, col = next_empty
                    self.board[row][col] = guess
                    if self.solver():
                        return True
                    self.board[row][col] = 0
                
        return False

def solve_sudoku(board):
    gameboard = Board(board)
    print(f'\nPuzzle to solve:\n{gameboard}')
    if gameboard.solver():
        print('\nSolved puzzle:')
        print(gameboard)
    else:
        print('\nThe provided puzzle is unsolvable.')
    
    return gameboard
#test_puzzle
puzzle = [
  [0, 0, 2, 0, 0, 8, 0, 0, 0],
  [0, 0, 0, 0, 0, 3, 7, 6, 2],
  [4, 3, 0, 0, 0, 0, 8, 0, 0],
  [0, 5, 0, 0, 3, 0, 0, 9, 0],
  [0, 4, 0, 0, 0, 0, 0, 2, 6],
  [0, 0, 0, 4, 6, 7, 0, 0, 0],
  [0, 8, 6, 7, 0, 4, 0, 0, 0],
  [0, 0, 0, 5, 1, 9, 0, 0, 8],
  [1, 7, 0, 0, 0, 6, 0, 0, 5]
]

solve_sudoku(puzzle)