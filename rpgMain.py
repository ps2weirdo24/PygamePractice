import pygame
import ptext
import rpgScene
import rpgResourceLoader

pygame.init()

DISPLAY_W = 704
DISPLAY_H = 704
FPS = 20

pygame.image.get_extended()

main_dipslay = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
pygame.display.set_caption("MyRPG")

Clock = pygame.time.Clock()

my_mixer = rpgResourceLoader.SoundHandler()

opening_music = my_mixer.load("aud_intense")
opening_music.set_volume(.5)


###########################

def game_loop():
	
	# 1. Take input
	# 2. Update game data
	# 3. Draw map / HUD
	# 4. Draw player
	pass



















###########################


def start_screen():
	opening_music.play()
	opening_screen = rpgScene.Menu("PyGame RPG", main_dipslay, ["Play the Game", "Quit the Game"])
	main_menu = rpgScene.Menu("Main Menu", main_dipslay, ["New Game","Load Game","Settings", "Quit to Desktop"])

	if opening_screen.run() == "Play the Game":
		if main_menu.run() == "New Game":
			opening_music.stop()
			game_loop()

	else:
		pass
		









start_screen()
pygame.quit()
quit()