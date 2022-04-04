class Square():
    """description of class"""
    def __init__(self, variation='', is_flagged=False, revealed=False, char='#'):
        self.is_flagged = is_flagged
        self.revealed = revealed
        self.char = char

    def __str__(self):
        return self.char

    def reveal(self):
        pass

    def flag(self):
        if not self.is_flagged and not self.revealed:
            self.is_flagged = True
            self.char = 'P'
        elif self.is_flagged:
            self.is_flagged = False
            self.char = '#'


class Bomb(Square):
    def __init__(self, is_flagged=False, revealed=False, char='x', variation='x'):
        super().__init__(is_flagged, revealed, char, variation)
        self.variation = 'x'
        self.is_flagged = is_flagged
        self.revealed = revealed
        if not self.revealed and not self.is_flagged:
            self.char = '#'
        elif is_flagged:
            self.char = 'P'

    def reveal(self, board):
        # Ends game
        if not self.is_flagged:
            self.revealed = True
            self.char = self.variation
            print('GAME OVER!')
            board.game_over = True
        

class Safe(Square):
    def __init__(self, surrounding_bombs=0, char=0, is_flagged=False, revealed=False, variation='s'):
        super().__init__(is_flagged, revealed, char, variation)
        self.surrounding_bombs = surrounding_bombs
        self.variation = 's'
        self.is_flagged = is_flagged
        self.revealed = revealed
        if not self.revealed and not self.is_flagged:
            self.char = '#'
        elif is_flagged:
            self.char = 'P'

    def reveal(self, board):
        if not self.is_flagged:
            self.revealed = True
            self.char = self.surrounding_bombs
            board.safe_squares -= 1

    def calculate_bombs(self, pos, gameboard):
        """Takes in position of current square and calculates ammount of bombs around it"""
        x, y = pos[0], pos[1]  # Currently doesn't have pos as varable
        surrounding_squares = [[x-1,y-1],[x,y-1],[x+1,y-1],
							   [x-1,y],			 [x+1,y],
							   [x-1,y+1],[x,y+1],[x+1,y+1]]  # Custom error for if index oversteps boundraries
        surrounding_bombs = 0
        for square in surrounding_squares:
            if square[0] >= gameboard.size or square[0] < 0:
                continue
            if square[1] >= gameboard.size or square[1] < 0:
                continue
            if gameboard.board[square[1]][square[0]].variation == 'x':
                surrounding_bombs +=1
        self.surrounding_bombs = surrounding_bombs