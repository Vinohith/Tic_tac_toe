import numpy as np 
from tic_tac_toe import tic_tac_toe


game = tic_tac_toe()
print(game.board)
game.toss()
print('Player ' + game.turn_moniter + ' starts.')
board, game_status = game.move(game.turn_moniter, (0,0))
print(board)
print(game_status)
board, game_status = game.move(game.turn_moniter, (0,1))
print(board)
print(game_status)
board, game_status = game.move(game.turn_moniter, (1,1))
print(board)
print(game_status)
board, game_status = game.move(game.turn_moniter, (0,2))
print(board)
print(game_status)
board, game_status = game.move(game.turn_moniter, (2,2))
print(board)
print(game_status)