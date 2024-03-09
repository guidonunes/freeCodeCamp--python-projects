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
        