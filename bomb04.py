import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

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

enemy_URL = 'resources/haha_images/brocole.png'
enemy_img = pygame.image.load(enemy_URL)
enemies = list()
#enemies = []
for cnt in range(3):
    enemy_pos = enemy_img.get_rect(left = 500 * cnt + 100, top = 100)
    enemies.append(enemy_pos)
    print(enemy_pos)
#enemy_pos = enemy_img.get_rect(left = 100, top = 100)

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

    for one in enemies:
        one.top += 6
        if one.bottom > SCREEN_HEIGHT:
            one.top = -100
            one.left = random.randint(0, SCREEN_WIDTH - enemy_img.get_width())


    screen.blit(player_img, player_pos)
    #screen.blit(enemy_img, enemy_pos)
    for one in enemies:
        screen.blit(enemy_img, one)
    pygame.display.flip()

    clock.tick(200)
