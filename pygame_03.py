import pygame

pygame.init()

width, height = 640, 480
size = (width, height)
screen = pygame.display.set_mode(size)

while True:
    WHITE = (255, 255, 255)
    screen.fill(WHITE)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)