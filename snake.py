import os
import keyboard

def clean_console():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

while True:
	event = keyboard.read_event()
	if event.event_type == keyboard.KEY_DOWN and event.name == "q":
		break;
	print(event.name)
	clean_console()
	
