import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 1280
SCREEN_HEIGHT= 720
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

player_url = 'resources/haha_images/mintchoco.png'
player_img = pygame.image.load(player_url)

while True:
    screen.fill(BLACK)

    event=pygame.event.poll()
    if event.type == pygame.QUIT:
        exit()

    screen.blit(player_img, (100, 100))

    pygame.display.flip()