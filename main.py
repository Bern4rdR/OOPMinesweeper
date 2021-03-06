from gameboard import *
from player import *
import os
import sys
import time

# Everything will go through the Board class
board = Board()
player = Player()

def tutorial():
	with open('tutorial.txt', 'rt') as tutorial:
		text = tutorial.readlines()

	for line in range(len(text)):
		if text[line] =='\n':
			print()
			continue
		if 1 <= line <= 11:
			if not line == 11:
				print(text[line].rstrip())
				continue
			print(text[line].rstrip(), end='')
			input()
			continue
		print(text[line].rstrip(), end='')
		input()


try: filesize = os.path.getsize("save.txt")
except: filesize = 0


if __name__ == '__main__':
	print(' WELCOME to acsii-minesweeper!')
	if input(' TUTORIAL [y/n]:  ').lower() == 'y':
		tutorial()

	if filesize > 1 and input(' You have a save file, would you like to load [y/n]:  ').lower() == 'y':
		player.score = board.load_game()
	else:
		board.start_game()

	while not board.game_over:
		print(board)
		print(f' SAFE SQUARES LEFT:  {board.safe_squares}')

		guess = player.guess(board.size)


		if guess is None:
			print('', end='')
		elif guess[0] == 'S':
			board.save_game()
			break

		elif guess[0] == 'L':
			board.load_game()
				
		elif len(guess) == 3:
			if guess[0]:
				board.board[guess[2]][guess[1]].reveal(board)
			elif not guess[0]:
				board.board[guess[2]][guess[1]].flag()

		board.update_time()
		print(' TIME: ', board.time_lapsed)
		player.calculate_score(board)

	time.sleep(.75)
	print(' LEADERBOARD:')
	player.see_leaderboard()
	if input(f'You got {player.score} score, do you want to post it? [y/n]').lower() == 'y':
		player.post_highscore()
	player.disconnect()