import pygame
import time

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill(WHITE)

BLOCK_SIZE = 20
block_red = pygame.Rect((1 * BLOCK_SIZE, 1 * BLOCK_SIZE),
                        (BLOCK_SIZE, BLOCK_SIZE))
pygame.draw.rect(screen, RED, block_red)
block_green = pygame.Rect((1 * BLOCK_SIZE, 3 * BLOCK_SIZE),
                        (BLOCK_SIZE, BLOCK_SIZE))
pygame.draw.rect(screen, GREEN, block_green)
block_blue = pygame.Rect((1 * BLOCK_SIZE, 5 * BLOCK_SIZE),
                        (BLOCK_SIZE, BLOCK_SIZE))
pygame.draw.rect(screen, BLUE, block_blue)

pygame.display.flip()

time.sleep(3)