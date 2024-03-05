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