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

