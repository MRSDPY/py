import pygame

display = pygame.display.set_mode((600, 600))
pygame.display.set_caption("SD New Experiment")


# FPS Setting
FPS = 50
clock = pygame.time.Clock()

# Player Settings
player_x = 50
player_y = 50
valocity_x = 0
valocity_y = 0
x_size = 20
y_size = 50

# Bullet
bullet_sx = 10
bullet_sy = 10
bullet_va = 0
bullet_x = player_x
bullet_y = player_y
fire_count = 0
fire_b = {}


# aim image
aim = pygame.image.load("Images/aim_r.png")

def set_aim(x, y):
	display.blit(aim, (x, y))

def fire(p_x, p_y, a_x, a_y):
	pass


while True:
	display.fill((255,255,255))
	
	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			pygame.quit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
				valocity_x = 5
				valocity_y = 0
			if event.key == pygame.K_UP or event.key == pygame.K_w:
				valocity_x = 0
				valocity_y = -5
			if event.key == pygame.K_LEFT or event.key == pygame.K_a:
				valocity_x = -5
				valocity_y = 0
			if event.key == pygame.K_DOWN or event.key == pygame.K_s:
				valocity_x = 0
				valocity_y = 5

		if event.type == pygame.MOUSEMOTION:
			pygame.mouse.set_visible(False)
			x, y = pygame.mouse.get_pos()
			set_aim(x, y)

		if event.type == pygame.MOUSEBUTTONDOWN:
			r, m, l = pygame.mouse.get_pressed()
			if r == 1:
				x, y = pygame.mouse.get_pos()
				bullet_x = player_x
				bullet_y = player_y
				print(x, y)
				fire_count += 1
				fire_b[fire_count] = {
					"sx": player_x,
					"sy": player_y,
					"dx": x,
					"dy": y,
				}


	
	player_x += valocity_x
	player_y += valocity_y

	if player_x > 580:
		player_x = 0
	elif player_x < 0:
		player_x = 580
	elif player_y > 580:
		player_y = 0
	elif player_y < 0:
		player_y = 580

	if fire_count > 0:
		for i in fire_b:
			bullet_x += fire_b[i]["d_x"]
			bullet_y -= fire_b[i]["d_y"]
			pygame.draw.rect(display, [255,0,0], [bullet_x+5, bullet_y-5, bullet_sx, bullet_sy])

	pygame.draw.rect(display, 
		[0,0,0], 
		[player_x, 
		player_y, 
		x_size, 
		y_size
		])
	clock.tick(FPS)
	pygame.display.update()

pygame.quit()
quit()