import pygame
import rpgImageLoader

pygame.init()

DISPLAY_W = 704
DISPLAY_H = 704
FPS = 20

pygame.image.get_extended()
MAIN_SCREEN = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
pygame.display.set_caption("MyRPG")

CLOCK = pygame.time.Clock()

imgloader = rpgImageLoader.ImageHandler()


def quit_to_desktop():
	pygame.quit()
	quit()

# GAMELOOP
