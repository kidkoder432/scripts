import pygame, sys, random, time
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()
fps = 60
pmovspd = 2
bmovspd = 7
window = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('Alien Shooter')
for event in pygame.event.get:
    if event.type == QUIT:
        pygame.quit()
        sys.exit()
    if event.type == KEYDOWN:
        if event.key == K_w or K_LEFT:
            
            


