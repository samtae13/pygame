import pygame

pygame.init()

width, height = 640, 480
size = (width, height)
screen = pygame.display.set_mode(size)

player = pygame.image.load('resources/images/dogdog.png')
player2 = pygame.image.load('resources/images/insta.png')

while True:
    screen.fill((0, 0, 0))
    screen.blit(player, (10, 10))
    screen.blit(player2, (330, 10))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)