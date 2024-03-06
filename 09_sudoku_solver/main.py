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