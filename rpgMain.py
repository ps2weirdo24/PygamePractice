import pygame
import ptext
import rpgScene
import rpgResourceLoader
import rpgHero
import rpgMap

pygame.init()

DISPLAY_W = 768
DISPLAY_H = 768
FPS = 60

pygame.image.get_extended()

main_dipslay = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
pygame.display.set_caption("MyRPG")

Clock = pygame.time.Clock()

my_mixer = rpgResourceLoader.SoundHandler()
img = rpgResourceLoader.ImageHandler()
my_map = rpgMap.MapHandler()

hud_img = img.get("Resources/images/img_rpg_gui_new.png")

level_music = my_mixer.load("aud_forest_song")
opening_music = my_mixer.load("aud_opening_menu")
opening_music.set_volume(.6)





def game_loop():
	main_dipslay.blit(hud_img, (0,0))

	while 1:
		process_game_state()
		render()
		hero.update()
		take_input()
		pygame.display.update()
		Clock.tick(FPS)

def render():
	base_layer = my_map.get_surface().copy()
	charx = int(hero.pos_x * 32)
	chary = int((hero.pos_y - 1) * 32)
	hero.idle_img.blit(base_layer, (charx, chary))
	main_dipslay.blit(base_layer, (32,32))

def take_input():
	for event in  pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				hero.facing = "left"
				if my_map.can_move_to((hero.pos_x-1), hero.pos_y):
					nice_move("left")
					hero.move("left")
				else:
					pass

			elif event.key == pygame.K_d:
				hero.facing = "right"
				if my_map.can_move_to((hero.pos_x+1), hero.pos_y):
					nice_move("right")
					hero.move("right")
				else:
					pass

			elif event.key == pygame.K_w:
				hero.facing = "up"
				if my_map.can_move_to(hero.pos_x, (hero.pos_y-1)):
					nice_move("up")
					hero.move("up")
				else:
					pass
			elif event.key == pygame.K_s:
				hero.facing = "down"
				if my_map.can_move_to(hero.pos_x, (hero.pos_y+1)):
					nice_move("down")
					hero.move("down")
				else:
					pass

			elif event.key == pygame.K_RETURN:
				pass
				#my_map.change_map(rpgMap.map_2_dir)

			elif event.key == pygame.K_ESCAPE:
				pygame.mixer.pause()
				pause_menu = rpgScene.Menu("Quit?", main_dipslay, ["Continue", "Save Game", "Quit to Desktop"]).run()
				if pause_menu == "Continue":
					pygame.mixer.unpause()
					render()
					game_loop()
				elif pause_menu == "Quit to Desktop":
					pygame.quit()
					quit()

def process_game_state():
	# Map Teleport Test
	if my_map.current_map == rpgMap.map_1_dir:
		if (hero.pos_x == 21) and (hero.pos_y == 17):
			my_map.change_map(rpgMap.map_2_dir)
			hero.pos_x = 0
			hero.pos_y = 17
		else:
			pass
	elif my_map.current_map == rpgMap.map_2_dir:
		if (hero.pos_x == 20) and (hero.pos_y == 18):
			my_map.change_map(rpgMap.map_3_dir)
			hero.pos_x = 1
			hero.pos_y = 1

	if (hero.pos_x == 2) and (hero.pos_y == 2):
		hero.current_health = 0
	# Death Test
	if hero.current_health == 0:
		game_over_scene = rpgScene.Menu("You Lose", main_dipslay, ["Press Enter to Quit", "wat"])
		if game_over_scene == "Press Enter to Quit":
			pygame.quit()
			quit()


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
		
def nice_move(direction):
	hero.update()
	render()
	pygame.display.update()
	start_x = hero.pos_x
	start_y = hero.pos_y
	if direction == "up":
		for i in range(10):
			hero.pos_y = (hero.pos_y - .1)
			render()
			pygame.display.update()
	elif direction == "down":
		for i in range(10):
			hero.pos_y = (hero.pos_y + .1)
			render()
			pygame.display.update()
	elif direction == "left":
		for i in range(10):
			hero.pos_x = (hero.pos_x - .1)
			render()
			pygame.display.update()
	elif direction == "right":
		for i in range(10):
			hero.pos_x = (hero.pos_x + .1)
			render()
			pygame.display.update()
	hero.pos_x = start_x
	hero.pos_y = start_y

hero = rpgHero.Hero()
start_screen()
pygame.quit()