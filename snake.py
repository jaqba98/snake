import os

def clean_console():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

while True:
	print("Map")
	clean_console()
	
