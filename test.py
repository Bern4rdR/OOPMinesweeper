from gameboard import *
from player import *

board = Board()
player = Player()

player.see_leaderboard()

player.score = 1550
player.name = 'Bernard R'

player.post_highscore()
player.disconnect()