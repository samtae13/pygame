import pygame

pygame.init

width, height = 640, 480
size = (width, height)
screen = pygame.display.set_mode(size)

player = pygame.image.load('resources/images/dude.png')
grass = pygame.image.load('resources/images/mic.png')
castle = pygame.image.load('resources/images/chicken_castle')

while True:
    screen.fill((0, 0, 0))

    grass_width = grass.get_width()
    grass_height = grass.get_height()
    for y in range(height // grass_height + 1):
        for x in range(width // grass_width + 1):
            screen.blit(grass, ())