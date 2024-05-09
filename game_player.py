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

	def move_player(self, key):
		if key == "w":
			self.y -= 1
		elif key == "s":
			self.y += 1
		elif key == "a":
			self.x -= 1
		elif key == "d":
			self.x += 1
		else:
			raise Exception("Not supported key for move the player: " + key)

