class Level:
	level_map = []

	def __init__(self, width, height):
		for y in range(height):
			level_map_line = []
			for x in range(width):
				level_map_line.append("")
			self.level_map.append(level_map_line)

class GameMap:
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def draw_game_map(self, g_player, appleX, appleY):
		game_map = []
		# Prepare the map area
		for y in range(self.height):
			game_map_line = []
			for x in range(self.width):
				if y == 0 or y == self.height - 1 or x == 0 or x == self.width - 1:
					game_map_line.append("#")
				elif x == appleX and y == appleY:
					game_map_line.append("@")
				else:
					game_map_line.append(" ")
			game_map.append(game_map_line)
		# Prepare the game_player
		gpx = g_player.x
		gpy = g_player.y
		game_map[gpy][gpx] = g_player.model
		# Draw the whole map
		game_map_lines = ""
		for y in range(self.height):
			game_map_line = ""
			for x in range(self.width):
				game_map_line += game_map[y][x]
			game_map_lines += game_map_line + "\n"
		print(game_map_lines)

