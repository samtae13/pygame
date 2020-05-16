import pygame
import os

WHITE = (255, 255, 255)
SCREEN_WIDTH = SCREEN_HEIGHT = 750
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

pygame.display.set_caption("SPACE INVADER")

# bg_img = pygame.image.load("resources/assets/background-black.png")
bg_img = pygame.image.load(os.path.join("resources", "assets", "background-black.png"))
bg_img = pygame.transform.scale(bg_img, (SCREEN_SIZE))

pygame.init()
pygame.font.init()
WIN = pygame.display.set_mode(SCREEN_SIZE)

while True:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            exit()

    WIN.blit(bg_img, (0, 0))

    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)

    lives_label = main_font.render(f"Lives: {lives}", 1, WHITE)
    level_label = main_font.render(f"Level: {level}", 1, WHITE)

    WIN.blit(lives_label, (10, 10))
    WIN.blit(level_label, (SCREEN_WIDTH - level_label.get_width() - 10, 10))

    pygame.display.update()