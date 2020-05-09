import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

score = 0
enemy_num = 1
gameover = False

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Premier Pro를 지켜라!!")
clock = pygame.time.Clock()
pygame.key.set_repeat(1)

small_font = pygame.font.SysFont("Agency FB", 36)
large_font = pygame.font.SysFont("HYNAML", 40)

pygame.key.set_repeat(1)

player_URL = 'resources/images/logo.png'
player_img = pygame.image.load(player_URL)
player_pos = player_img.get_rect(centerx = SCREEN_WIDTH // 2, bottom = SCREEN_HEIGHT)

enemy_URL = 'resources/images/nodap.png'
enemy_img = pygame.image.load(enemy_URL)
enemies_info = []
for cnt in range(enemy_num):
    enemy_info = enemy_img.get_rect(left = random.randint(0, SCREEN_WIDTH-enemy_img.get_width()),
                                   bottom = -100 * cnt)
    enemy_speed = random.randint(5, 15)
    enemies_info.append([enemy_info, enemy_speed])

pygame.mixer.init()
bgm_URL = 'resources/audio/error.mp3'
pygame.mixer.music.load(bgm_URL)
pygame.mixer.music.play(-1)

while True:
    screen.fill(BLACK)

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        if not gameover and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_pos.left -= 5
            elif event.key == pygame.K_RIGHT:
                player_pos.left += 5
            if player_pos.left < 0:
                player_pos.left = 0
            elif player_pos.right > SCREEN_WIDTH:
                player_pos.right = SCREEN_WIDTH

    if not gameover:
        for one in enemies_info:
            one[0].top += 6
            if one[0].bottom > SCREEN_HEIGHT:
                one[0].top = -100
                one[0].left = random.randint(0, SCREEN_WIDTH - enemy_img.get_width())
                one[0].top = -100
                one[1] = random.randint(5, 15)
                score += 1
                if (score % 8 == 0):
                    enemy_info = enemy_img.get_rect(left=random.randint(0, SCREEN_WIDTH - enemy_img.get_width()),
                                                    bottom=-200)
                    enemy_speed = random.randint(5, 15)
                    enemies_info.append([enemy_info, enemy_speed])



    for one in enemies_info:
        if one[0].colliderect(player_pos):
            gameover = True


    screen.blit(player_img, player_pos)
    #screen.blit(enemy_img, enemy_pos)
    for one in enemies_info:
        screen.blit(enemy_img, one[0])

    score_img = small_font.render("score: {}".format(score), True, YELLOW)
    screen.blit(score_img, (10, 10))

    if gameover:
        gameover_img = large_font.render("당신의 프리미어가 응답없음을 표시했습니다...", True, YELLOW)
        screen.blit(gameover_img, (SCREEN_WIDTH // 2 - gameover_img.get_width() // 2,
                                   SCREEN_HEIGHT // 2 - gameover_img.get_height() // 2))

    pygame.display.flip()
    clock.tick(144)