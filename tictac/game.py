
import uuid
games = {}

WIN_POS = [
       (1, 2, 3),
       (4, 5, 6),
       (7, 8, 9),
       (1, 4, 7),
       (2, 5, 8),
       (3, 6, 9),
       (1, 5, 9),
       (3, 5, 7),
    ]

messages = {
	201: 'Move succeeded',
	204: 'Game over ',
	400: 'Invalid move or player',
	403: 'Move not allowed',
	409: 'Game tied'

}


def get_all():
	games_list=dict()
	for k,v in games.items():
		games_list[k] = v.players
	return games_list


def upsert(game):
	games[game.Id] = game


def delete(g_id):
	games.pop(g_id)


def read(g_id):
	return games.get(g_id)


class Game(object):

	def __init__(self):
		self.Id = str(uuid.uuid4().fields[-1])[:5]
		self.players = []
		self.board = list(range(0, 10))
		self.winner = None
		self.last_player = None

	def _check_win(self):
		for a, b, c in WIN_POS:
			if self.board[a] == self.board[b] == self.board[c]:
				return True
		return False

	def _tie(self):
		if len(self.players) == 2:
			p1 = self.board.count(self.players[0])
			p2 = self.board.count(self.players[1])
			if (p1+p2) == 9:
				return True
		return False

	def move(self,player, pos):
		if not player:
			return 400

		if not (1 <= pos <= 9):
			return 400

		if player not in self.players:
			if len(self.players) < 2:
				self.players.append(player)
			else:
				return 400

		if player == self.last_player:
			return 403

		# check if other player is in pos
		if self.board[pos] in self.players:
			return 400  # taken

		self.board[pos] = player
		if self._check_win():
			self.winner = player
			return 200  # game over

		if self._tie():
			self.winner = 'tie'
			upsert(self)
			return 409

		self.last_player = player
		upsert(self)
		return 201

	def current(self):
		def code(j):
			p1 = p2 = None
			if len(self.players) == 2:
				p1 = self.players[0]
				p2 = self.players[1]
			elif len(self.players) == 1:
				p1 = self.players[0]

			if j == p1:
				return ' x'
			elif j == p2:
				return ' o'
			else:
				return '__'

		out = {}
		b = self.board
		for i in range(1,10,3):
			out[i] = code(b[i])+code(b[i+1])+code(b[i+2])
		return out
