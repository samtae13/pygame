import pygame
import time

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 300
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

BLOCK_SIZE = 10

def draw_block(screen, color, position):
    block_rect = pygame.Rect((position[0] * BLOCK_SIZE, position[1] * BLOCK_SIZE),
                             (BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, color, block_rect)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

for bx in range(0, SCREEN_WIDTH // BLOCK_SIZE + 1, 2):
    for by in range(0, SCREEN_HEIGHT // BLOCK_SIZE + 1, 2):
        draw_block(screen, GREEN, (bx , by))
        draw_block(screen, RED, (bx + 1, by))
        draw_block(screen, RED, (bx, by + 1))
        draw_block(screen, GREEN, (bx + 1, by + 1))
        time.sleep(0.0000001)
        pygame.display.flip()



time.sleep(3)