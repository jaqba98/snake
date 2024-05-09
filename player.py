class Tail:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Player:
	tails = []

	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def add_tail(self, x, y):
		newTail = Tail(x, y)
		self.tails.append(newTail)

	def move_player(self, direction):
		if direction == "up":
			self.y -= 1
		elif direction == "down":
			self.y += 1
		elif direction == "left":
			self.x -= 1
		elif direction == "right":
			self.x += 1
		else:
			raise Exception("Not supported direction: " + direction)

