import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

# set screen icon and title
pygame.display.set_caption("MR.SD Space Invaders")

running_status = True

# while running_status:
#     screen.fill((0, 0, 0))

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running_status = False

pygame.mixer.music.load("sd d.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(1.0)
while pygame.mixer.music.get_busy(): 
    pygame.time.Clock().tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_status = False

# pygame.time.delay(30)
pygame.display.update()