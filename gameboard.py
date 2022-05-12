import random
import math
import time
import os
from square import *

DIFFICULTY = {
    'easy' : 0.1,
    'medium' : 0.2,
    'hard' : 0.3
    }

class Board():
    """The game board contains all the general information about the game"""
    def __init__(self, size=10, bombs=20, start_time=time.time(), time_lapsed=0, board=[], game_over=False):
        self.size = size
        self.bombs = bombs
        self.safe_squares = size**2 - bombs
        self.start_time = start_time
        self.end_time = time.time()
        self.time_lapsed = time_lapsed + (self.end_time - self.start_time)
        self.board = board
        self.game_over = game_over


    def __str__(self):
        ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        retstr = '    '
        for i in range(self.size):
            retstr +=f'  {ALPHABET[i]} '
        retstr += '\n    ' + '+---'*self.size + '+\n'
        for row in self.board:
            row_int = self.board.index(row) + 1
            retstr += (2-len(str(row_int)))*' ' + f' {row_int}' + ' | '
            for element in row:
                retstr += f'{element.char} | '
            retstr += '\n    '
            retstr += '+---'*self.size + '+\n'
        return retstr


    def start_game(self):
        self.game_over = False
        self.board_size()
        self.game_diff()
        self.generate_board()


    def board_size(self):
        while True:
            size_input = input(' CHOOSE A BOARD SIZE (recomended: 5 - 15):  ')
            if size_input == '':
                print(' STANDARD:  10x10')
                break
            else:
                try: self.size = int(size_input)
                except: 
                    print(' INVALID INPUT!')
                if self.size <= 1:
                    print(' INVALID INPUT! (too small of a size)')
                elif self.size > 26:
                    print(' INVALID INPUT! (exceeded max size)')
                else:
                    break


    def game_diff(self):
        difficulty = input(' CHOOSE DIFFICULTY [easy/medium/hard]:  ').lower()  # use difflib
        if difficulty == '':
            print(' STANDARD:  medium')
        elif difficulty.isdigit() and 1 <= int(difficulty) < 100:
            self.bombs = math.ceil((self.size**2) * (int(difficulty)/100))
            print(f' CUSTOM:  {difficulty}%')
        else:
            try: self.bombs = math.ceil((self.size**2) * DIFFICULTY[difficulty.replace(' ', '')])
            except: 
                print(' INVALID INPUT! (check your spelling)')
                self.game_diff()
        self.safe_squares = self.size**2 - self.bombs


    def generate_board(self):
        self.board = [[Safe([x, y]) for x in range(self.size)] for y in range(self.size)]
        self.generate_bombs()

        for y in range(self.size):
            for x in range(self.size):
                if not self.board[y][x].variation == 'x':
                    self.board[y][x].calculate_bombs(self)

    def generate_bombs(self):
        placed = 0
        while placed < self.bombs:
            x, y = random.randint(0,self.size-1), random.randint(0,self.size-1)
            if not self.board[y][x].variation == 'x':
                self.board[y][x] = Bomb([x, y])
                placed +=1


    def clear_board():
        pass


    def reveal_bombs():  # for when player looses
        pass


    def update_time(self):
        self.end_time = time.time()
        self.time_lapsed += (self.end_time - self.start_time)
        self.start_time = time.time()


    def save_game(self):
        try: filesize = os.path.getsize("save.txt")
        except: filesize = 0
        board_state = []
        save = True

        if filesize > 1 and input(' You already have a save file, do you want to override [y/n]:  ').lower() == 'n':
            save = False
                
        if save:
            for y in self.board:
                for x in y:
                    flagged_state = 'f'
                    revealed_state = 'r'
                    if x.is_flagged: flagged_state = 'F'
                    if x.revealed: revealed_state = 'R'
                    board_state.append(f'{flagged_state}{revealed_state}{x.variation}')
            self.update_time()
            board_state += [self.size, self.safe_squares, self.time_lapsed]  # time, safe squares, size, etc

            with open('save.txt', 'wt+') as file:
                for square in board_state:
                    file.write(f'{square}\n')
            print(' GAME SAVED ...')


    def load_game(self):
        """When loading the game, the load will be deleted as to prevent 
        repeated tries"""
        self.board = []
        with open('save.txt', 'rt+') as file:
            board_state = file.readlines()
            #file.truncate(0)  # deletes the save file   - - - - - - [ temporarily disabled for testing ] - - - - - -
        self.size = int(board_state[-3].rstrip())
        self.safe_squares = int(board_state[-2].rstrip())

        index = 0
        for y in range(self.size):
            row = []
            for x in range(self.size):
                flag, reveal, type = board_state[index].rstrip()
                if type == 's':
                    row.append(Safe([x, y], flag.istitle(), reveal.istitle()))
                elif type == 'x':
                    row.append(Bomb([x, y], flag.istitle()))  # bomb will never be revealed
                index += 1
            self.board.append(row)

        for y in range(self.size):
            for x in range(self.size):
                if not self.board[y][x].variation == 'x':
                    self.board[y][x].calculate_bombs(self)
                    self.board[y][x].update()

        print(' GAME LOADED ...')
        return float(board_state[-1].rstrip())
