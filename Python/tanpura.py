import pygame.mixer
import pygame, os
os.chdir(r'c:\users\findp\onedrive\documents\prajwal_files\scripts\python')
from pygame.locals import *
pygame.init()
x = 0
speeds = [100, 150, 175, 180]
tppl = False
tbpl = False
taals = ['tabla']
taal = taals[0]
speed = speeds[0]
pygame.display.set_mode((600,600), pygame.RESIZABLE)
tp = pygame.mixer.Sound('gtanpura.wav')
tb = pygame.mixer.Sound('tabla100.wav')
print('Playing...')
tp.set_volume(0.2)
tb.set_volume(1)

print('''
Press S to start/stop tabla
Press W to start/stop tanpura
Press F to change Taal
Press R to change speeds
Press Esc to quit''')
while True:
    #print('Taal: ' + taal + ' ' + str(speed) + ' bpm', end='\r')
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()
            elif event.key == K_r:
                tb.stop()
                speed = speeds[x % len(speeds)]
                tb = pygame.mixer.Sound(taal + str(speed) + '.wav')
                x += 1
                tbpl = False

                print('Taal: ' + taal + ' ' + str(speed) + ' bpm')
            elif event.key == K_w:
                tppl = not tppl
                if tppl:
                    tp.play(-1)
                else:
                    tp.stop()
            elif event.key == K_s:
                tbpl = not tbpl
                if tbpl:
                    tb.play(-1)
                else:
                    tb.stop()
    pygame.display.update()
