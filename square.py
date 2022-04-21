UNKNOWN_CHAR = '-'
FLAGGED_CHAR = 'P'

class Square():
    """Original square instance, populates the game board"""
    def __init__(self, pos, is_flagged=False, revealed=False, char=UNKNOWN_CHAR, variation=''):
        self.pos = pos
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
            self.char = FLAGGED_CHAR
        elif self.is_flagged:
            self.is_flagged = False
            self.char = UNKNOWN_CHAR


class Bomb(Square):
    def __init__(self, pos, is_flagged=False, revealed=False, char='x', variation='x'):
        super().__init__(pos, is_flagged, revealed, char, variation)
        self.pos = pos
        self.variation = 'x'
        self.is_flagged = is_flagged
        self.revealed = revealed
        if not self.revealed and not self.is_flagged:
            self.char = UNKNOWN_CHAR
        elif is_flagged:
            self.char = FLAGGED_CHAR


    def reveal(self, board):
        # Ends game
        if not self.is_flagged:
            self.revealed = True
            self.char = self.variation
            print(' GAME OVER!')
            board.game_over = True
        

class Safe(Square):
    def __init__(self, pos, is_flagged=False, revealed=False, surrounding_bombs=0, char=' ', variation='s'):
        super().__init__(pos, is_flagged, revealed, char, variation)
        self.pos = pos
        self.surrounding_bombs = surrounding_bombs
        self.variation = 's'
        self.is_flagged = is_flagged
        self.revealed = revealed
        self.update()


    def reveal(self, board, original=True):  # original is used to check if it's first in chain-reveal
        if not self.is_flagged and not self.revealed:
            self.revealed = True
            self.update()
            board.safe_squares -= 1

            if self.char == ' ':  # clear multiple
                clear_ammount = board.safe_squares + 1
                x, y = self.pos
                surrounding_squares = [[x-1,y-1],[x,y-1],[x+1,y-1],
							           [x-1,y],			 [x+1,y],
							           [x-1,y+1],[x,y+1],[x+1,y+1]]
                for square in surrounding_squares:
                    if not (0 <= square[0] < board.size):
                        continue
                    if not (0 <= square[1] < board.size):
                        continue
                    board.board[square[1]][square[0]].reveal(board, False)
                if original:
                    print(f' CLEARED:  {clear_ammount - board.safe_squares} squares')


    def update(self):
        if not self.revealed and not self.is_flagged:
            self.char = UNKNOWN_CHAR
        elif self.is_flagged:
            self.char = FLAGGED_CHAR
        elif self.revealed:
            if self.surrounding_bombs > 0:
                self.char = self.surrounding_bombs
            else:
                self.char = ' '


    def calculate_bombs(self, gameboard):
        """Takes in position of current square and calculates amount of bombs around it"""
        x, y = self.pos
        surrounding_squares = [[x-1,y-1],[x,y-1],[x+1,y-1],
							   [x-1,y],			 [x+1,y],
							   [x-1,y+1],[x,y+1],[x+1,y+1]]
        surrounding_bombs = 0
        for square in surrounding_squares:
            if square[0] >= gameboard.size or square[0] < 0:
                continue
            if square[1] >= gameboard.size or square[1] < 0:
                continue
            if gameboard.board[square[1]][square[0]].variation == 'x':
                surrounding_bombs +=1
        self.surrounding_bombs = surrounding_bombs