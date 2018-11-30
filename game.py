import numpy as np 
from pprint import pprint
from tic_tac_toe import tic_tac_toe


def legal_move_generator(current_board_state, turn_moniter):
	legal_moves_dict = {}
	for i in range(current_board_state.shape[0]):
		for j in range(current_board_state.shape[1]):
			if current_board_state[(i,j)] == '_':
				current_board_state_copy = np.copy(current_board_state)
				# current_board_state_copy = current_board_state.copy()
				current_board_state_copy[(i,j)] = turn_moniter
				legal_moves_dict[(i,j)] = current_board_state_copy.flatten()
	return legal_moves_dict


game = tic_tac_toe()
print(game.board)
game.toss()
print('Player ' + game.turn_moniter + ' starts.')

# Test 1 (for tic_tac_toe class)
# board, game_status = game.move(game.turn_moniter, (0,0))
# print(board)
# print(game_status)
# board, game_status = game.move(game.turn_moniter, (0,1))
# print(board)
# print(game_status)
# board, game_status = game.move(game.turn_moniter, (1,1))
# print(board)
# print(game_status)
# board, game_status = game.move(game.turn_moniter, (0,2))
# print(board)
# print(game_status)
# board, game_status = game.move(game.turn_moniter, (2,2))
# print(board)
# print(game_status)

# test 2 (for function legal_move_generator)
legal_moves_dict = legal_move_generator(game.board, game.turn_moniter)
print('Legal moves : ')
pprint(legal_moves_dict)
print(legal_moves_dict[0,1][1])