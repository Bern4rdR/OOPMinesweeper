from gameboard import *
from player import *
# Everything will go through the Board class
# Use __str__() to print board
board = Board()
player = Player()

board.generate_board()

while not board.game_over:
	print(board)

	guess = player.guess(board)

	if guess[0]:
		# just revels square - can be a bomb or not
		board.board[guess[2]][guess[1]].reveal(board)

	elif not guess[0]:
		board.board[guess[2]][guess[1]].flag()

print(board.safe_squares)