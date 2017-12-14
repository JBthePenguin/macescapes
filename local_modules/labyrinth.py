import os

""" Module with the class Labyrinth"""

class Labyrinth():
	"""docstring for Labyrinth
	__init__()"""
	def __init__(self):
		""" Function : initialise an object with attribute zones {}"""
		self.zones = {}
		main_directory = os.path.dirname(os.path.dirname(__file__)) # we get the right path...
		path_to_file = os.path.join(main_directory, "maps", "default_map.txt")
		with open(path_to_file, "r") as f: # ...and we open the file
			x = 0
			y = 0
			for elt in f.read():
				if elt == "\n":
					x = 0
					y += 1
				else:
					if elt == "O":
						self.zones[(x,y)] = "wall"
					else:
						self.zones[(x,y)] = "background"
					x += 1
