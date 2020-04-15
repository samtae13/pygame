import pygame
import time

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 80
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

screen.fill(WHITE)

#pygame.Rect((x, y), (width, height))

green_rect = pygame.Rect((10, 10), (30, 30))
red_rect = pygame.Rect((310, 40), (80, 30))
pygame.draw.rect(screen, GREEN, green_rect)
pygame.draw.rect(screen, RED, red_rect)

pygame.display.flip()
time.sleep(3)