import pygame, time

pygame.init()
width, height = 1024, 600
size = (width, height)
screen = pygame.display.set_mode(size)

pygame.draw.rect(screen, (200, 200, 200), [10, 10, 50, 50], 2)
pygame.display.flip()

time.sleep(2)