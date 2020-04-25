import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

pygame.key.set_repeat(1)

player_URL = 'resources/haha_images/mintchoco.png'
player_img = pygame.image.load(player_URL)
player_pos = player_img.get_rect(centerx = SCREEN_WIDTH // 2, bottom = SCREEN_HEIGHT)

while True:
    screen.fill(BLACK)

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        exit()
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player_pos.left -= 5
        elif event.key == pygame.K_RIGHT:
            player_pos.left += 5
        if player_pos.left < 0:
            player_pos.left = 0
        elif player_pos.right > SCREEN_WIDTH:
            player_pos.right = SCREEN_WIDTH


    screen.blit(player_img, player_pos)
    pygame.display.flip()

    clock.tick(60)