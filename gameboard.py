import random
from square import *

class Board():
    """The gameboard contains all the general information about the game"""
    def __init__(self, size=10, bombs=20, time=[0,0], board=[], game_over=False):
        self.size = size
        self.bombs = bombs
        self.safe_squares = size**2 - bombs
        self.time = time  # WIP
        self.board = board
        self.game_over = game_over

    def __str__(self):
        retstr = '+---'*self.size + '+\n'
        for row in self.board:
            retstr += '| '
            for element in row:
                retstr += f'{element.char} | '
            retstr += '\n'
            retstr += '+---'*self.size + '+\n'
        return retstr

    def compare_input(self):
        pass

    def generate_board(self):
        self.board = [[Safe() for x in range(self.size)] for y in range(self.size)]
        self.generate_bombs()

        for y in range(self.size):
            for x in range(self.size):
                if not self.board[y][x].variation == 'x':
                    self.board[y][x].calculate_bombs([x,y], self)

    def generate_bombs(self):
        placed = 0
        while placed < self.bombs:
            x, y = random.randint(0,self.size-1), random.randint(0,self.size-1)
            if not self.board[y][x].variation == 'x':
                self.board[y][x] = Bomb()
                placed +=1

    def clear_board():
        pass

    def reveal_bombs():
        pass

    def save_game():
        pass

    def load_game():
        pass