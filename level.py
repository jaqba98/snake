class Level:
	level_map = []

	def __init__(self, width, height):
		self.width = width
		self.height = height

	def init_level_map(self, player):
		self.level_map = []
		for y in range(self.height):
			level_map_line = []
			for x in range(self.width):
				level_map_line.append(" ")
			self.level_map.append(level_map_line)
		self.add_border()
		self.add_player(player)

	def add_border(self):
		for y in range(len(self.level_map)):
			for x in range(len(self.level_map[y])):
				if x == 0 or x == len(self.level_map[y]) - 1 or y == 0 or y == len(self.level_map) - 1:
					self.level_map[y][x] = "#"

	def add_player(self, player):
		self.level_map[player.y][player.x] = player.model
		for tail in player.tails:
			self.level_map[tail.y][tail.x] = player.model
	def draw_level_map(self):
		level_map_lines = ""
		for y in range(len(self.level_map)):
			level_map_line = ""
			for x in range(len(self.level_map[y])):
				level_map_line += self.level_map[y][x]
			level_map_lines += level_map_line + "\n"
		print(level_map_lines)

