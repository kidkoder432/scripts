import pygame.mixer
import pygame
from pygame.locals import *
pygame.init()
tppl = tbpl = False
pygame.display.set_mode((600,600))
tp = pygame.mixer.Sound('gtanpura.wav')
tb = pygame.mixer.Sound('tabla.wav')
print('Playing...')
tp.set_volume(0.4)
print('''
Press S to stop tabla
Press D to start tabla
Press W to stop tanpura
Press E to play tanpura
Press R to change Taal
Press F to change speed.''')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            raise Exception('Quit.')
        elif event.type == KEYDOWN:
            if event.key == K_w:
                tppl = not tppl
##            elif event.key == K_e:
##                tp.play(-1)
            elif event.key == K_s:
                tbpl = not tbpl
##            elif event.key == K_d:
##                  tb.play(-1)
    if tppl:
        tp.play(-1)
    elif tbpl:
        tb.play(-1)
    else:
        tb.stop()
        tp.stop()
    
                    
    

