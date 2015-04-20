import pygame

pygame.init()

#color definitions

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

display_width = 1200
display_height = int(display_width * .75)
block_size = 10 
FPS = 20

pygame.image.get_extended()

pygame.display.set_caption("Adventures of Bob")

gameExit = False

clock = pygame.time.Clock()

#pygame.mixer.music.load("resources/music/gamemusic.ogg")
#pygame.mixer.music.set_volume(.5)
#pygame.mixer.music.play(loops = -1)

lead_x = display_width/2
lead_x_change = 0
lead_y = display_height/2
lead_y_change = 0

while not gameExit:

	for event in  pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				lead_x_change -= block_size
				#lead_y_change = 0
			elif event.key == pygame.K_RIGHT:
				lead_x_change += block_size
				#lead_y_change = 0
			elif event.key == pygame.K_UP:
				lead_y_change -= block_size
				#lead_x_change = 0
			elif event.key == pygame.K_DOWN:
				lead_y_change += block_size
				#lead_x_change = 0
			elif event.key == pygame.K_SPACE:
				lead_x_change = -lead_x
				lead_y_change = -lead_y

	if lead_x >= display_width or lead_x <= 0 or lead_y >= display_height or lead_y <= 0:
		gameExit = True



	lead_x += lead_x_change
	lead_y += lead_y_change	

	gameDisplay.fill(white)
	pygame.draw.rect(gameDisplay, black, [lead_x,lead_y,10,10])

	pygame.display.update()
	clock.tick(FPS)

pygame.quit()
quit()