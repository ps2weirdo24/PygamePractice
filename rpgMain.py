import pygame
import ptext
import rpgScene

pygame.init()

DISPLAY_W = 704
DISPLAY_H = 704
FPS = 20

pygame.image.get_extended()
MAIN_SCREEN = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
pygame.display.set_caption("MyRPG")

Clock = pygame.time.Clock()


opening_screen = rpgScene.Menu("PyGame RPG", MAIN_SCREEN, ["Play the Game", "Quit the Game"])
main_menu = rpgScene.Menu("Main Menu", MAIN_SCREEN, ["New Game","Load Game","Settings", "Quit to Desktop"])

if opening_screen.run() == "Play the Game":
	main_menu.run()
else:
	pygame.quit()
	quit()










pygame.quit()
quit()