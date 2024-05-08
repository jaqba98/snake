import os
import keyboard

map_width = 50
map_height = 50

player_x = 5
player_y = 5

def clean_console():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

def display_map():
	for y in range(map_width):
		line = ""
		for x in range(map_height):
			if x == player_x and y == player_y:
				line += "P"
			else:
				line += " "
		print(line)

while True:
	event = keyboard.read_event()
	if event.event_type == keyboard.KEY_DOWN:
		if event.name == "q":
			break;
		elif event.name == "w":
			player_y -= 1
		elif event.name == "s":
			player_y += 1
		elif event.name == "a":
			player_x -= 1
		elif event.name == "d":
			player_x += 1
	clean_console()
	display_map()
	
