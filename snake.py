import os
import keyboard
import time
import threading

map_width = 50
map_height = 20

player_x = 5
player_y = 5

direction = "w"

def clean_console():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

def display_map():
	map = ""
	topLine = ""
	for x in range(map_width):
		topLine += "#"

	map += topLine + "\n"
	for y in range(map_height):
		line = ""
		for x in range(map_width):
			if x == 0:
				line += "#"
			if x == player_x and y == player_y:
				line += "P"
			elif x == map_width - 2:
				line += "#"
			else:
				line += " "
		map += line + "\n"
	map += topLine + "\n"
	print(map)

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

while True:
	if direction == "w":
		player_y -= 1
	elif direction == "s":
		player_y += 1
	elif direction == "a":
		player_x -= 1
	elif direction == "d":
		player_x += 1
	
	clean_console()
	display_map()
	time.sleep(0.1)
