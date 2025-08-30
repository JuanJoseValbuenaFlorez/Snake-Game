import pygame, sys, random
from pygame.math import Vector2

pygame.init()

BG_COLOR = (173,204,96)
SNAKE_COLOR = (43,52,24)

cell_size = 30
numbre_of_cells = 25

screen = pygame.display.set_mode((cell_size * numbre_of_cells, cell_size *  numbre_of_cells,))

pygame.display.set_caption("retro snake")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(BG_COLOR)
    
    pygame.display.update()
    clock.tick(60)