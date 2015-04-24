# This file will handle menus and other scenes that might fit the classes

import pygame
import ptext
import rpgResourceLoader


FPS = 20
Clock = pygame.time.Clock()
img = rpgResourceLoader.ImageHandler()
mixer = rpgResourceLoader.SoundHandler()

cursor_sound = mixer.load("aud_menu_select")
select_sound = mixer.load("aud_menu_confirm")


class Menu:
	def __init__(self, menu_title, surface, options):
		"""
		The "options" argument has to be a list of strings, this list 
		will be the options the user has to pick from.
		"""
		self.source_surface = surface
		self.title = str(menu_title)
		self.options = options
		self.total_options = int(len(options) - 1)
		self.current_option = 0
		self.selection_made = False
		self.user_selection = None

		
		self.base_surface = img.get("Resources/images/img_title_screen.bmp")
		self.cursor = img.get("Resources/images/img_menu_cursor2.bmp")

		

	def take_input(self):
		for event in  pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					cursor_sound.play()
					pass
				elif event.key == pygame.K_d:
					cursor_sound.play()
					pass
				elif event.key == pygame.K_w:
					cursor_sound.play()
					if self.current_option == 0:
						pass
					else:
						self.current_option = (self.current_option - 1)
					
				elif event.key == pygame.K_s:
					cursor_sound.play()
					if self.current_option == self.total_options:
						pass
					else:
						self.current_option = (self.current_option + 1)
					
				elif event.key == pygame.K_RETURN:
					select_sound.play()
					self.user_selection = str(self.options[int(self.current_option)])
					self.selection_made = True
					
					
				# elif event.key == pygame.K_ESCAPE:
				# 	pygame.quit()
				# 	quit()


	def render(self):
		x_offset = 32
		y_offset = 32
		self.source_surface.blit(self.base_surface, (x_offset,y_offset))
		ptext.draw(self.title, top=(64 + y_offset), centerx=(352 + (x_offset/2)), fontsize = 72.0, color="black")
		loop_x = (352 + (x_offset/2))
		loop_y = (256 + y_offset)
		for item in self.options:
			ptext.draw(str(item), centerx=loop_x, centery=loop_y, fontsize = 48, color="black")
			loop_y = (loop_y + 64)
		arrow_y = (64*int(self.current_option)) + (256 + y_offset) - (int(self.cursor.get_height())/2)
		arrow_x = int(loop_x - 152)
		self.source_surface.blit(self.cursor, (arrow_x, arrow_y))


	
	def run(self):
		self.source_surface.fill(pygame.Color(0, 0, 0))
		pygame.display.update()
		while not self.selection_made:
			self.take_input()
			self.render()
			pygame.display.update()
			Clock.tick(FPS)
		self.source_surface.fill(pygame.Color(0, 0, 0))
		pygame.display.update()
		return str(self.user_selection)







