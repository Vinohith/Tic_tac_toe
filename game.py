import numpy as np 
from pprint import pprint
from tic_tac_toe import tic_tac_toe

from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import SGD


def legal_move_generator(current_board_state, turn_moniter):
	legal_moves_dict = {}
	for i in range(current_board_state.shape[0]):
		for j in range(current_board_state.shape[1]):
			if current_board_state[(i,j)] == '_':
				current_board_state_copy = np.copy(current_board_state)
				# current_board_state_copy = current_board_state.copy()
				current_board_state_copy[(i,j)] = turn_moniter
				legal_moves_dict[(i,j)] = current_board_state_copy.flatten()
	for move in legal_moves_dict:
		# print(list(legal_moves_dict[move]))
		legal_moves_dict[move] = np.array([1 if i!='_' else 2 for i in list(legal_moves_dict[move])])
		# print(list(legal_moves_dict[move]))
	return legal_moves_dict


model = Sequential()
model.add(Dense(18, input_dim = 9, kernel_initializer = 'normal', activation = 'relu'))
model.add(Dropout(0.1))
model.add(Dense(9, kernel_initializer = 'normal', activation = 'relu'))
model.add(Dropout(0.1))
model.add(Dense(1, kernel_initializer = 'normal'))

sgd = SGD(lr = 0.001, momentum = 0.8)
model.compile(loss = 'mean_squared_error', optimizer=sgd)
model.summary()



def move_selector(model, current_board_state, turn_moniter):
	tracker = {}
	legal_moves_dict = legal_move_generator(current_board_state, turn_moniter)
	for move in legal_moves_dict:
		score = model.predict(legal_moves_dict[move].reshape(1,9))
		tracker[move] = score
	selected_move = max(tracker)
	new_board_state = legal_moves_dict[selected_move]
	score = tracker[selected_move]
	return selected_move, new_board_state, score



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

# test 3 (evaluator)
selected_move,new_board_state,score=move_selector(model, game.board, game.turn_moniter)
print('Selected move : ', selected_move)
print("Resulting new board state: ",new_board_state)
print("Score assigned to above board state by Evaluator(model): ", score)