import time

import level
import system

fps = 60
interval = 1 / fps

g_level = level.Level(50, 20)

while True:
	start_time = time.time();

	system.clear_console_screen()
	g_level.draw_level_map()

	elapsed_time = time.time() - start_time
	time.sleep(max(0, interval - elapsed_time))

# Fix

import player

import os
import keyboard
import threading
import random

import level

direction = "w"
run = True

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
score = 0

appleX = 0
appleY = 0

while run == True:
	system.clear_console_screen()
	
	print(score)
	if (appleX == 0 and appleY == 0) or g_player.x == appleX and g_player.y == appleY: 
		#appleX = random.randrange(1, g_map.width - 2)
		#appleY = random.randrange(1, g_map.height - 2) 
		score += 1	
		#g_player.add_tail(g_player.x, g_player.y)
		
	g_player.move_player(direction, g_map)

	print(len(g_player.tails))
	time.sleep(0.1)

system.clear_console_screen()

