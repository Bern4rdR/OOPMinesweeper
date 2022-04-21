PPB = 100  # Points Per Bomb
TP = 5  # Time Points (decreases with this much every second)
FP = 10  # Flag Points (decreases with this much every time a flag is placed)

class Player():
    """description of class"""
    def __init__(self, name='Anonymous', score=0):
        self.name = name
        self.score = score


    def format_input(self, input, size):  # RETURN FORMAT: [True/False, X, Y] (reveal/-not, X-pos, Y-pos)
        ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        border = ALPHABET[:size]
        input.replace(' ', '')

        try:
            first_num = [x.isdigit() for x in input].index(True)
        except:
            print(' INVALID INPUT! (no number found)')
            return self.guess(size)  # bad practice?

        if first_num == 1 and input[first_num] != '0':  # clear
            if input[0].upper() in set(border) and (1 <= int(input[first_num:]) <= size):
                 return [True, ALPHABET.find(input[0].upper()), int(input[first_num:])-1]  # True means reveal

            elif input[:first_num].upper() not in set(border) or not (1 <= int(input[first_num:]) <= size):
                print(' INPUT IS OUT OF BOUNDS')
                return self.guess(size)

        elif first_num == 2 and input[first_num] != '0' and input[0].upper() == 'F':  # flag
            return [False, ALPHABET.find(input[1:first_num].upper()), int(input[first_num:])-1]  # False means flag
       
        else:
            print(' INVALID FORMAT!')
            return self.guess(size)


    def guess(self, size):
        guess = input(' INPUT:  ')
        if guess.lower() == 'save':  # might spell-check
            return 'S'
        elif guess.lower() == 'load':
            return 'L'
        return self.format_input(guess, size)
        

    def calculate_score(self, board):  # recalculates every time (won't need to be saved)
        max_score = PPB * board.bombs
        pps = max_score / (board.size**2 - board.bombs)  # Points Per Square (cleared)
        self.score = max_score - pps * board.safe_squares - TP * board.time_lapsed #- FP * [flag count]
        print(f' SCORE:  {self.score}')


    def post_highscore(self):
        pass