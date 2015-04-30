###############
# This class will handle the loading of the maps and provide 
# information about collision and changing maps 
# 
###############
import pygame
import rpgResourceLoader

img = rpgResourceLoader.ImageHandler()

# I currently only have two maps and will load them into this file manually 
# maybe I should build a map loader in the future?
 
img_map_1 = img.get("Resources/map/map_1/img_new_map_1.bmp")
txt_map_1 = "Resources/map/map_1/txtmap_1.txt"

img_map_2 =img.get("Resources/map/map_2/img_new_map_2.bmp")
txt_map_2 = "Resources/map/map_2/txtmap_2.txt"

def decode_txt(file_location):
	nest_map_1 = []
	map_txt_file = open(str(file_location), "r")
	mytry = map_txt_file.readlines()
	map_txt_file.close()
	cleantry = []
	for item in mytry:
		newitem = item[:int(len(item)-1)]
		cleantry.append(newitem)
	map_1_height = len(cleantry)
	map_1_width = len(cleantry[0])
	for i in range(map_1_width):
		nest_map_1.append([])
	for line in cleantry:
		for i in range(len(line)):
			nest_map_1[i].append(line[i])
	return nest_map_1

map_1_dir = ["map_1", img.get("Resources/map/map_1/img_new_map_1.bmp"), "Resources/map/map_1/txtmap_1.txt"]
map_2_dir = ["map_2", img.get("Resources/map/map_2/img_new_map_2.bmp"), "Resources/map/map_2/txtmap_2.txt"]
map_3_dir = ["map_3", img.get("Resources/map/map_3/img_new_map_3.bmp"), "Resources/map/map_3/txtmap_3.txt"]

class MapHandler:
	def __init__(self):
		self.current_map = map_1_dir
		self.layout = decode_txt(self.current_map[2])
		self.current_surface = self.current_map[1]
		self.width = len(self.layout)
		self.height = len(self.layout[0])
		
	def get_surface(self):
		return self.current_surface

	def can_move_to(self, pos_x, pos_y):
		"""
		This func takes 2 args, pos_x and pos_y, these args are refering to the position on the map
		this func will return a boolean value stating if the position provided in the args is able
		to be occupied or not
		True = can be occupied
		False =  can not be occupied
		"""
		if (pos_x > (self.width - 1)) or (pos_x < 0) or (pos_y > (self.height - 1)) or (pos_y < 0):
			return False
		else:
			can_move_test = self.layout[pos_x][pos_y]
			if can_move_test == "x":
				return False
			elif (can_move_test == "o") or (can_move_test == "t"):
				return True


	def is_teleport(self, pos_x,pos_y):
		can_tele_test = self.layout[pos_x][pos_y]
		if can_tele_test == "t":
			return True
		else:
			return False

	def change_map(self, new_map):
		self.current_map = new_map
		self.layout = decode_txt(self.current_map[2])
		self.current_surface = self.current_map[1]
		self.width = len(self.layout)
		self.height = len(self.layout[0])




if __name__=="__main__":
	debug = MapHandler()

