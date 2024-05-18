import level

g_level = level.Level(50, 50)

g_level.draw_level_map()

# Fix

import player

import os
import keyboard
import time
import threading
import random

import system
import level

direction = "w"
run = True

def clean_console():
	if system.get_system_name()  == "windows":
		os.system("cls")
	elif system.get_system_name() == "unix":
		os.system("clear")

def monitor_keyboard_events():
	global direction
	global run
	while True:
		if keyboard.is_pressed("w"):
			direction = "w"
		if keyboard.is_pressed("s"):
			direction = "s"
		if keyboard.is_pressed("a"):
			direction = "a"
		if keyboard.is_pressed("d"):
			direction = "d"
		if keyboard.is_pressed("e"):
			run = False

keyboard_thread = threading.Thread(target=monitor_keyboard_events)
keyboard_thread.daemon = True
keyboard_thread.start()

print("Snake in Python v0.1")
print("Author: Jakub Olejarczyk")
print("----------------------------")
map_width = int(input("Enter the map width: "))
map_height = int(input("Enter the map height: "))

g_player  = player.Player(10, 10, "$")
g_map = level.GameMap(map_width, map_height)
score = 0

appleX = 0
appleY = 0

while run == True:
	clean_console()
	
	print(score)
	if (appleX == 0 and appleY == 0) or g_player.x == appleX and g_player.y == appleY: 
		appleX = random.randrange(1, g_map.width - 2)
		appleY = random.randrange(1, g_map.height - 2) 
		score += 1	
		g_player.add_tail(g_player.x, g_player.y)
		
	g_player.move_player(direction, g_map)

	g_map.draw_game_map(g_player, appleX, appleY)
	print(len(g_player.tails))
	time.sleep(0.1)

clean_console()

