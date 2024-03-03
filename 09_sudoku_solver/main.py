class Board:
    #instantiate object to a customized state
    def __init__(self, board):
        self.board = board
        
    def __str__(self):
    #create the top border of the board
        upper_lines = f'\n╔═══{"╤═══"*2}{"╦═══"}{"╤═══"*2}{"╦═══"}{"╤═══"*2}╗\n'