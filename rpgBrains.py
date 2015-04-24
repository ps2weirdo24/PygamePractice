import pygame
import rpgResourceLoader
import ptext
import pyganim
import rpgScene

img = rpgResourceLoader.ImageHandler()
mxr = rpgResourceLoader.SoundHandler()

class Hero:
	"""
	Name = Main Character
	Health = 100/100
	Mana = 100/100
	Attack Power = 1
	Defense Power = 1
	Level = 1

	Position_x = 4
	Position_y = 12
	"""
	def __init__(self):

		self.name = "Main Character"
		self.current_health = 100
		self.max_health = 100
		self.current_mana = 50
		self.max_mana = 50
		self.attack_pow = 1
		self.def_pow = 1
		self.level = 1

		self.facing = "down"
		self.pos_x = 1
		self.pos_y = 2
		self.height = 64
		self.width = 32


		self.icon = img.get("Resources/images/characters/character_icons/img_char_2.bmp")
		self.master_sheet = img.get("Resources/images/characters/img_hero_sheet.png")

		self.bin_step = 0
		self.foot_0 = mxr.load("aud_footstep_dirt_00")
		self.foot_1 = mxr.load("aud_footstep_dirt_01")
		self.foot_2 = mxr.load("aud_footstep_dirt_02")
		self.foot_3 = mxr.load("aud_footstep_dirt_03")
		self.foot_4 = mxr.load("aud_footstep_dirt_04")
		self.foot_5 = mxr.load("aud_footstep_dirt_05")
		self.foot_6 = mxr.load("aud_footstep_dirt_06")
		self.foot_7 = mxr.load("aud_footstep_dirt_07")
		self.foot_8 = mxr.load("aud_footstep_dirt_08")
		self.foot_9 = mxr.load("aud_footstep_dirt_09")
		self.foot_container = [self.foot_0, self.foot_1, self.foot_2, self.foot_3, 
								self.foot_4, self.foot_5, self.foot_6, 
								self.foot_7, self.foot_8, self.foot_9]

		frame_list = []
		col_trans = pygame.Color("#0080ff")
		for x in range(32):
			if (x < 8):
				cir_x = 0
				cir_y = int(x*32)
			elif (x >= 8) and (x < 16):
				cir_x = 64
				cir_y = int((x-8)*32)
			elif (x >= 16) and (x < 24):
				cir_x = 128
				cir_y = int((x-16)*32)
			elif (x >= 24) and (x < 32):
				cir_x = 192
				cir_y = int((x-24)*32)
			else:
				print "yikes"

			single_surface = pygame.Surface((32, 64))
			single_surface.blit(self.master_sheet, (0, 0), (cir_y, cir_x, 32, 64))
			single_surface.set_colorkey(col_trans)
			frame_list.append(single_surface)

		self.frames = frame_list

		# 1 2 3 1 4 5
		self.animate_up = pyganim.PygAnimation([(self.frames[2], .2), 
												(self.frames[1], .2), 
												(self.frames[0], .2), 
												(self.frames[2], .2), 
												(self.frames[3], .2), 
												(self.frames[4], .2)])
		self.animate_up.play()

		self.animate_down = pyganim.PygAnimation([(self.frames[10], .2), 
												  (self.frames[9], .2), 
												  (self.frames[8], .2), 
												  (self.frames[10], .2), 
												  (self.frames[11], .2), 
												  (self.frames[12], .2)])
		self.animate_down.play()

		self.animate_right = pyganim.PygAnimation([(self.frames[16], .2), 
												  (self.frames[17], .2), 
												  (self.frames[18], .2), 
												  (self.frames[19], .2), 
												  (self.frames[20], .2), 
												  (self.frames[21], .2),
												  (self.frames[22], .2),
												  (self.frames[23], .2)])
		self.animate_right.play()

		self.animate_left = pyganim.PygAnimation([(self.frames[24], .2), 
												  (self.frames[25], .2), 
												  (self.frames[26], .2), 
												  (self.frames[27], .2), 
												  (self.frames[28], .2), 
												  (self.frames[29], .2),
												  (self.frames[30], .2),
												  (self.frames[31], .2)])
		self.animate_left.play()










		self.idle_img = self.frames[10]

	def step_sound(self):
		(self.foot_container[self.bin_step]).play()
		if self.bin_step == 9:
			self.bin_step = 0
		else:
			self.bin_step = (self.bin_step + 1) 


	def move(self, direction):
		if self.facing == direction:
			if direction == "left":
				if self.pos_x == 1:
					pass
				else:
					self.pos_x = (self.pos_x - 1)
					self.step_sound()
			elif direction == "up":
				if self.pos_y == 2:
					pass
				else:
					self.animate_up.play()
					self.pos_y = (self.pos_y - 1)
					self.step_sound()
			elif direction == "right":
				if self.pos_x == 20:
					pass
				else:
					self.pos_x = (self.pos_x + 1)
					self.step_sound()
			elif direction == "down":
				if self.pos_y == 18:
					pass
				else:
					self.pos_y = (self.pos_y + 1)
					self.step_sound()

		else:
			self.facing = direction

	def update(self):
		if self.facing == "left":
			self.idle_img = self.animate_left
		elif self.facing == "up":
			self.idle_img = self.animate_up
		elif self.facing == "right":
			self.idle_img = self.animate_right
		elif self.facing == "down":
			self.idle_img = self.animate_down

class Game_Map:
	def __init__(self):

		self.width = 22
		self.height = 20
		self.current_map = "map_1"
		self.map_surface = img.get("Resources/map/map_1/img_map_1.bmp")








if __name__ == "__main__":
	my_test = Hero()
	my_test2 = Game_Map()


