class Player():
    """description of class"""
    def __init__(name, score=0):
        pass

    def tutorial():
        pass

    def format_input(self, input, board):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        input.replace(' ', '')
        print(input)
        if len(input) == 2:
            if input[0].lower() in set(alphabet[:board.size]):  # and input[1] is in range(1, size)
                 return [True, alphabet.find(input[0].lower()), int(input[1])-1]  # True means reveal
            elif input[0].lower() in set(alphabet[board.size:]):  # or input[1] is larger than size
                print('out of bounds')
        elif len(input) == 3 and input[0].lower() == 'f':  # flag
            return [False, alphabet.find(input[1].lower()), int(input[2])-1]  # False means flag
        else:
            print('INCORRECT FORMAT!')
        # return input

    def guess(self, board):
        guess = input('INPUT:  ')
        return self.format_input(guess, board)
        

    def calculate_score(self):
        pass

    def post_highscore(self):
        pass