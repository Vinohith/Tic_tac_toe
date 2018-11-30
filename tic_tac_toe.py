import numpy as np


class tic_tac_toe():
	def __init__(self):
		self.board = np.full((3,3), '_')
		self.player0 = 'x'
		self.player1 = 'o'

	def toss(self):
		turn = np.random.randint(0,2)
		if turn == 0:
			self.turn_moniter = self.player0
		elif turn == 1:
			self.turn_moniter = self.player1
		return self.turn_moniter

	def move(self, player, cord):
		if self.board[cord] != '_' or self.turn_moniter != player or self.game_status() != 'In progress':
			raise ValueError('Invalid')
		if player == 'x':
			self.board[cord] = self.player0
			self.turn_moniter = self.player1
		elif player == 'o':
			self.board[cord] = self.player1
			self.turn_moniter = self.player0
		return self.board, self.game_status()

	def game_status(self):
		for i in range(self.board.shape[0]):
			if '_' not in self.board[i, :] and len(set(self.board[i, :])) == 1:
				return 'Won'
		for j in range(self.board.shape[1]):
			if '_' not in self.board[:, j] and len(set(self.board[:, j])) == 1:
				return 'Won'
		if '_' not in np.diag(self.board) and len(set(np.diag(self.board))) == 1:
			return 'Won'
		if '_' not in np.diag(np.fliplr(self.board)) and len(set(np.diag(np.fliplr(self.board)))) == 1:
			return 'Won'

		if '_' not in self.board:
			return 'Draw'
		else:
			return 'In progress'