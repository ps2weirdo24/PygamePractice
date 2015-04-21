# This module will be used to load all the images into the game
# This module will want to be updated often as the structure of folders will change
 
import pygame

pygame.image.get_extended()


origin_file_dict = {"hud":"Resources/images/img_hud.bmp", 
			 "menu":"Resources/images/img_menu.bmp",
			 "menu_cursor":"Resources/images/img_menu_cursor2.bmp",
			 "plain_menu":"Resources/images/img_plain_menu.bmp",
			 "map_1":"Resources/map/map_1/img_map_1.bmp",
			 "map_2":"Resources/map/map_2/img_map_2.bmp",
			 "map_3":"Resources/map/map_3/img_map_3.bmp",
			 "dungeon_tiles":"Resources/map/tiles/img_dungeon_tiles.png",
			 "main_char_up":"Resources/images/characters/hero/img_hero_up.bmp",
			 "main_char_down":"Resources/images/characters/hero/img_hero_down.bmp",
			 "main_char_left":"Resources/images/characters/hero/img_hero_left.bmp",
			 "main_char_right":"Resources/images/characters/hero/img_hero_right.bmp"}




class ImageHandler():

	def __init__(self):
		self.file_dir = origin_file_dict
		self.surface_dict = {}
		for pairs in self.file_dir.items():
			self.surface_dict[str(pairs[0])] = pygame.image.load(str(pairs[1]))

	def get(self, str_key):
		this_key = str(str_key)
		if self.surface_dict.has_key(this_key):
			return self.surface_dict[this_key]
		else:
			print "ERROR: The key '%s' was not found in the ImageHandler Dictionary" % this_key

	def get_all(self):
		return self.file_dir






