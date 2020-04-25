import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

player_URL = 'resources/haha_images/mintchoco.png'
player_img = pygame.image.load(player_URL)
player_pos = player_img.get_rect()

player_pos.left = SCREEN_WIDTH // 2 - (player_img.get_width() // 2)
player_pos.top = SCREEN_HEIGHT -  player_img.get_height()

while True:
    screen.fill(BLACK)

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        exit()

    screen.blit(player_img, player_pos)
    pygame.display.flip()