import os
import keyboard
import time
import threading

import system
import game_player
import game_map

map_width = 50
map_height = 20

direction = "w"

player2 = game_player.GamePlayer(5, 5, "d")

def clean_console():
	if system.get_system_name()  == "windows":
		os.system("cls")
	elif system.get_system_name() == "unix":
		os.system("clear")

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

print("Snake in Python v0.1")
print("Author: Jakub Olejarczyk")
print("----------------------------")
map_width = int(input("Enter the map width: "))
map_height = int(input("Enter the map height: "))

g_player  = game_player.GamePlayer(10, 10, "$")
g_map = game_map.GameMap(map_width, map_height)

while True:
	clean_console()
	g_player.move_player(direction)
	g_map.draw_game_map(g_player)
	time.sleep(0.1)

#while True:
	#oldX = player2.x
	#oldY = player2.y
	#player2.move_player(direction)

	#if len(player2.tails) < 15:	
#		player2.add_tail(oldX, oldY)
	
	#oldTile = player.Tail(oldX, oldY)
	#for tile in player2.tails:
	#	x = oldTile.x
	#	y = oldTile.y
	#	oldTile = player.Tail(tile.x, tile.y)
	#	tile.x = x
	#	tile.y = y
