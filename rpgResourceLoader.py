# This module will be used to load all the images into the game
# This module will want to be updated often as the structure of folders will change
 
import pygame
import os

pygame.image.get_extended()

sfx_dir = "Resources/audio/sound_effects"
music_dir = "Resources/audio/music"



origin_file_dict = {"hud":"Resources/images/img_hud.bmp", 
			 "menu":"Resources/images/img_menu.bmp",
			 "menu_cursor":"Resources/images/img_menu_cursor2.bmp",
			 "plain_menu":"Resources/images/img_title_screen.bmp",
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
			return pygame.image.load(str_key)

	def get_all(self):
		return self.file_dir





class SoundHandler():

	def __init__(self):
		if pygame.mixer.get_init() == None:
			pygame.mixer.init()
		else:
			pass
		find_sfx_list = os.listdir(sfx_dir)
		find_music_list = os.listdir(music_dir)
		self.sfx_dict = {}
		self.music_dict = {}
		for item in find_sfx_list:
			new_item = (sfx_dir + "/" + item)
			self.sfx_dict[item[0:(len(item)-4)]] = new_item
		for item in find_music_list:
			new_item = (music_dir + "/" + item)
			self.music_dict[item[0:(len(item)-4)]] = new_item

	def load(self, sound_filename):
		"""
		This will return a pygame.Sound object
		"""
		if sound_filename in self.sfx_dict:
			file_to_load = self.sfx_dict[sound_filename]
		elif sound_filename in self.music_dict:
			file_to_load = self.music_dict[sound_filename]
		else:
			file_to_load = sound_filename

		return pygame.mixer.Sound(file_to_load)


