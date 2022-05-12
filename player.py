import socket
import math

PPB = 100  # Points Per Bomb
TP = 5  # Time Points (decreases with this much every second)
FP = 10  # Flag Points (WIP: decreases with this much every time a flag is placed)

HEADER = 64
PORT = 5050
SERVER = ''
FORMAT = 'utf-8'
DISCONNECT_MSG = '!DISCONNECT'
LEADERBOARD_MSG = '!LEADERBOARD'
POST_MSG = '!POST'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def connect():
    try: 
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(ADDR)
    except: None


def send(msg):
	message = msg.encode(FORMAT)
	msg_length = len(message)
	send_length = str(msg_length).encode(FORMAT)
	send_length += b' ' * (HEADER - len(send_length))
	client.send(send_length)
	client.send(message)
	
	msg_len = client.recv(HEADER).decode(FORMAT)  # Information on how long the message is
	if msg_len:
		msg_len = int(msg_len)
		recieve_msg = client.recv(msg_len).decode(FORMAT)
		if recieve_msg:
			return recieve_msg
	else:
		return None


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
            return self.guess(size)

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
        elif guess.lower() == 'post':
            self.post_highscore()
            return None
        elif guess.lower() == 'leaderboard':
            self.see_leaderboard()
            return None
        else: return self.format_input(guess, size)

    def calculate_score(self, board):  # recalculates every time (won't need to be saved)
        max_score = PPB * board.bombs
        pps = max_score / (board.size**2 - board.bombs)  # Points Per Square (cleared)
        self.score = math.floor(max_score - pps * board.safe_squares - TP * board.time_lapsed) #- FP * [flag count]
        print(f' SCORE:  {self.score}')


    def post_highscore(self):  # Receives the placement and tells the user
        print(send(POST_MSG + f'{self.name} {self.score}'))


    def see_leaderboard(self):
        return_msg = send(LEADERBOARD_MSG)
        if return_msg is not None:
            print(return_msg.replace('-', '\n'))

    def disconnect(self):
        send(DISCONNECT_MSG)