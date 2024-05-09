import os
import keyboard
import time
import threading

import system

map_width = 50
map_height = 20

direction = "d"

class Tail:
	tails = []
	def __init__(self, x, y):
		self.x = x
		self.y = y

player = Tail(5, 5)

def clean_console():
	if system.get_system_name()  == "windows":
		os.system("cls")
	elif system.get_system_name() == "unix":
		os.system("clear")

def display_map():
	map = []
	for y in range(map_height):
		currMap = []
		for x in range(map_width):
			if x == 0 or x == map_width - 1 or y == 0 or y == map_height - 1:
				currMap.append("#")
			else:
				currMap.append(" ")
		map.append(currMap)

	map[player.y][player.x] = "P";

	for tail in player.tails:
		map[tail.y][tail.x] = "O"
	
	mapStr = ""
	for y in range(map_height):
		mapLine = ""
		for x in range(map_width):
			mapLine = mapLine + map[y][x]
		mapStr = mapStr + "\n" + mapLine

	print(mapStr)

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
	oldX = player.x
	oldY = player.y
	if direction == "w":
		player.y -= 1
	elif direction == "s":
		player.y += 1
	elif direction == "a":
		player.x -= 1
	elif direction == "d":
		player.x += 1

	if len(player.tails) < 15:	
		player.tails.append(Tail(oldX, oldY));
	
	oldTile = Tail(oldX, oldY)
	for tile in player.tails:
		x = oldTile.x
		y = oldTile.y
		oldTile = Tail(tile.x, tile.y)
		tile.x = x
		tile.y = y

	clean_console()
	display_map()
	time.sleep(0.1)
