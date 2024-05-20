import time
import keyboard
import threading

import level
import system
import player

direction = "w"
 
def monitor_keyboard_events():
	global direction
	while True:
		if keyboard.is_pressed("w"):
			direction = "w"
		if keyboard.is_pressed("s"):
			direction = "s"
		if keyboard.is_pressed("a"):
			direction = "a"
		if keyboard.is_pressed("d"):
			direction = "d"

keyboard_thread = threading.Thread(target=monitor_keyboard_events)
keyboard_thread.daemon = True
keyboard_thread.start()

g_player = player.Player(10, 10, "@")
g_level = level.Level(50, 20)

while True:
	system.clear_console_screen()
	g_level.init_level_map(g_player)
	g_level.draw_level_map()
	g_player.move_player(direction)
	time.sleep(0.1)

