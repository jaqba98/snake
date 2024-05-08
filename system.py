import os

def get_system_name():
	if os.name == "posix": return "unix"
	if os.name == "nt": return "widnows"
	raise Exception("Not supported os.name = " + os.name)

