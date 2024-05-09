class Tail:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class GamePlayer:
	tails = []

	def __init__(self, x, y, model):
		self.x = x
		self.y = y
		self.model = model
	
	def add_tail(self, x, y):
		newTail = Tail(x, y)
		self.tails.append(newTail)

	def move_player(self, key, g_map):
		if key == "w":
			if self.y == 1:
				self.y = g_map.height - 2
			else:
				self.y -= 1
		elif key == "s":
			if self.y == g_map.height - 2:
				self.y = 1
			else:
				self.y += 1
		elif key == "a":
			if self.x == 1:
				self.x = g_map.width - 2
			else:
				self.x -= 1
		elif key == "d":
			if self.x == g_map.width - 2:
				self.x = 1
			else:
				self.x += 1
		else:
			raise Exception("Not supported key for move the player: " + key)

