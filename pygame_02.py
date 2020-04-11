import pygame

pygame.init()

width, height = 800, 600
size = (width, height)
screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)