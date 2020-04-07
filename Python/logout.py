import pygame, pyautogui, time
from pygame.locals import *
pygame.init()
prev = time.time()
for event in pygame.event.get():
    while (event.type == KEYDOWN or event.type == MOUSEMOTION) and not isTimeout():
        print(now)        
        
    