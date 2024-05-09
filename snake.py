import os
import keyboard
import time
import threading

import system
import player

map_width = 50
map_height = 20

direction = "d"

player2 = player.Player(5, 5)

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

	map[player2.y][player2.x] = "P";

	for tail in player2.tails:
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
	oldX = player2.x
	oldY = player2.y
	if direction == "w":
		player2.y -= 1
	elif direction == "s":
		player2.y += 1
	elif direction == "a":
		player2.x -= 1
	elif direction == "d":
		player2.x += 1

	if len(player2.tails) < 15:	
		player2.add_tail(oldX, oldY)
	
	oldTile = player.Tail(oldX, oldY)
	for tile in player2.tails:
		x = oldTile.x
		y = oldTile.y
		oldTile = player.Tail(tile.x, tile.y)
		tile.x = x
		tile.y = y

	clean_console()
	display_map()
	time.sleep(0.1)
