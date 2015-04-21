# This file will handle menus and other scenes that might fit the classes

import pygame
import ptext
import rpgResourceLoader


FPS = 20
Clock = pygame.time.Clock()
img = rpgResourceLoader.ImageHandler()


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

		
		self.base_surface = img.get("plain_menu")
		self.cursor = img.get("menu_cursor")

		

	def take_input(self):
		for event in  pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					pass
				elif event.key == pygame.K_d:
					pass
				
				elif event.key == pygame.K_w:
					if self.current_option == 0:
						pass
					else:
						self.current_option = (self.current_option - 1)
					
				elif event.key == pygame.K_s:
					if self.current_option == self.total_options:
						pass
					else:
						self.current_option = (self.current_option + 1)
					
				elif event.key == pygame.K_RETURN:
					self.user_selection = str(self.options[int(self.current_option)])
					self.selection_made = True
					
					
				elif event.key == pygame.K_ESCAPE:
					pygame.quit()
					quit()


	def render(self):
		self.source_surface.blit(self.base_surface, (0,0))
		ptext.draw(self.title, top=64, centerx=352, 
					fontname="Resources/fonts/vgasys.fon", fontsize = 72.0, color="black")
		loop_x = 256
		loop_y = 352
		for item in self.options:
			ptext.draw(str(item), top=loop_x, centerx=loop_y,
						fontname="Resources/fonts/vgasys.fon", fontsize = 48, color="black")
			loop_x = (loop_x + 64)
		arrow_x = (64*int(self.current_option)) + 246
		arrow_y = int(loop_y - 128)
		self.source_surface.blit(self.cursor, (arrow_y, arrow_x))


	
	def run(self):
		while not self.selection_made:
			self.take_input()
			self.render()
			pygame.display.update()
			Clock.tick(FPS)
		return str(self.user_selection)







