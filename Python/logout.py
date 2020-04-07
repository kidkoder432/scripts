import pygame, pyautogui, time
from pygame.locals import *
def isTimeout():
for event in pygame.event.get():
    while (event.type == KEYDOWN or event.type == MOUSEMOTION) and not isTimeout():
        event = pygame.event.get()        
        
    