import time
import threading
import random
import readchar

import level
import system
import player
import apple

direction = "w"
 
g_player = player.Player(10, 10, "@")
g_level = level.Level(50, 20)
g_apple = apple.Apple(15, 15, "o")

def read_key():
	global direction
	while True:
		direction = readchar.readkey()

key_reader_thread = threading.Thread(target=read_key, daemon=True)
key_reader_thread.start()

while True:
	system.clear_console_screen()
	if g_player.x == g_apple.x and g_player.y == g_apple.y:
		g_apple.x = random.randrange(1, g_level.width)
		g_apple.y = random.randrange(1, g_level.height)
		g_player.add_tail(g_player.x, g_player.y)

	prev_x = g_player.x
	prev_y = g_player.y
	for i in range(len(g_player.tails)):
		old_x = g_player.tails[i].x
		old_y = g_player.tails[i].y
		g_player.tails[i].x = prev_x
		g_player.tails[i].y = prev_y
		prev_x = old_x
		prev_y = old_y

	g_level.init_level_map(g_player, g_apple)
	g_level.draw_level_map()
	g_player.move_player(direction, g_level)
	time.sleep(0.1)

