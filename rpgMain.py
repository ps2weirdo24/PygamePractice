import pygame
import ptext
import rpgScene
import rpgResourceLoader
import rpgBrains

pygame.init()

DISPLAY_W = 768
DISPLAY_H = 768
FPS = 20

pygame.image.get_extended()

main_dipslay = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
pygame.display.set_caption("MyRPG")

Clock = pygame.time.Clock()

my_mixer = rpgResourceLoader.SoundHandler()
img = rpgResourceLoader.ImageHandler()

hud_img = img.get("Resources/images/img_rpg_gui_new.png")

level_music = my_mixer.load("aud_forest_song")
opening_music = my_mixer.load("aud_opening_menu")
opening_music.set_volume(.6)





def game_loop():
	main_dipslay.blit(hud_img, (0,0))

	while 1:
		render()
		hero.update()
		take_input()
		pygame.display.update()
		Clock.tick(FPS)


def render():
	base_layer = game_map.map_surface.copy()
	charx = int(hero.pos_x * 32)
	chary = int((hero.pos_y - 1) * 32)
	hero.idle_img.blit(base_layer, (charx, chary))
	#hero.animate_up.blit(base_layer, (charx, chary))
	main_dipslay.blit(base_layer, (32,32))

def take_input():
	for event in  pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				#
				hero.move("left")

			elif event.key == pygame.K_d:
				#
				hero.move("right")

			elif event.key == pygame.K_w:
				#
				hero.move("up")

			elif event.key == pygame.K_s:
				#
				hero.move("down")

			elif event.key == pygame.K_RETURN:
				#
				pass

			elif event.key == pygame.K_ESCAPE:
				pygame.mixer.pause()
				if rpgScene.Menu("Quit?", main_dipslay, ["Continue", "Save Game", "Quit to Desktop"]).run() == "Continue":
					pygame.mixer.unpause()
					render()
					game_loop()
				elif rpgScene.Menu("Quit?", main_dipslay, ["Continue", "Save Game", "Quit to Desktop"]).run() == "Quit to Desktop":
					pygame.quit()
					quit()


###########################


def start_screen():
	opening_music.play()
	opening_screen = rpgScene.Menu("PyGame RPG", main_dipslay, ["Play the Game", "Quit the Game"])
	main_menu = rpgScene.Menu("Main Menu", main_dipslay, ["New Game","Load Game","Settings", "Quit to Desktop"])
	

	if opening_screen.run() == "Play the Game":
		if main_menu.run() == "New Game":
			opening_music.fadeout(1000)
			level_music.play(loops=-1)
			game_loop()

	else:
		pass
		








game_map = rpgBrains.Game_Map()
hero = rpgBrains.Hero()
start_screen()
pygame.quit()