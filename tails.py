import tail

class Tails:
	tails = []

	def add_tail(self, x, y):
		newTail = tail.Tail(x, y)
		self.tails.append(newTail)

