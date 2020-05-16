import pygame
import os
import random

WHITE = (255, 255, 255)
SCREEN_WIDTH = SCREEN_HEIGHT = 750
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

pygame.display.set_caption("SPACE INVADER")

pygame.init()
pygame.font.init()
WIN = pygame.display.set_mode(SCREEN_SIZE)

bg_img = pygame.image.load(os.path.join("resources", "assets", "background-black.png"))
bg_img = pygame.transform.scale(bg_img, SCREEN_SIZE)

YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("resources", "assets", "pixel_ship_yellow.png"))

RED_SPACE_SHIP = pygame.image.load(os.path.join("resources", "assets", "pixel_ship_red_small.png"))

class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []

    def draw(self, window):
        #pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, 50, 50))
        window.blit(self.ship_img, (self.x, self.y))

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.max_health = health

class Enemy(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = RED_SPACE_SHIP

    def move(self, vel):
        self.y +=  vel

def main():
    run = True
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)

    enemies = []
    wave_length = 5
    enemy_vel = 1

    player_vel = 8
    player = Player(300, 650)

    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(bg_img, (0, 0))

        lives_label = main_font.render(f"Lives: {lives}", 1, WHITE)
        level_label = main_font.render(f"Level: {level}", 1, WHITE)
        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (SCREEN_WIDTH - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(WIN)
        player.draw(WIN)

        pygame.display.update()

    while run:
        clock.tick(144)
        redraw_window()

        if len(enemies) == 0:
            wave_length += 2
            for i in range(wave_length):
                enemy = Enemy(random.randint(50, 700), random.randint(-1000, -10))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0:
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel < SCREEN_WIDTH - player.get_width():
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > 0:
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel < SCREEN_HEIGHT - player.get_width():
            player.y += player_vel

        for enemy in enemies:
            enemy.move(enemy_vel)
            if enemy.y > SCREEN_HEIGHT:
                enemies.remove(enemy)

main()