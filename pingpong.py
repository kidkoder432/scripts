import pygame, random, time
from pygame.locals import *
pygame.init()
d = 0
py, cy = 0, 0
ps, cs = 0, 0
pu, pd = False, False
x = 250
y = 250
screen = pygame.display.set_mode([500, 500])
playerPaddle = pygame.draw.rect(screen, (128, 0, 0), (485, py, 10, 140))
compPaddle = pygame.draw.rect(screen, (128, 0, 0), (485, cy, 10, 140))
ball = pygame.draw.circle(screen, (0, 0, 255), (x, y), 10)
font = pygame.font.SysFont(None, 30)
xa, ya = random.randint(1, 10000) / 10000, random.randint(1, 10000) / 10000


def physics(p, b):
    global x, y, xa, ya, ps, cs, d
    if b.colliderect(p):
        xa = abs(xa) * -1
        x = 474
    elif x > 500:
        xa = abs(xa) * -1
        x = 250
        y = 250
        d = 1
        ps -= 1
        
        
    elif x < 0:
        xa = abs(xa)
        x = 250
        y = 250
        d = 1
        ps += 1
        
        #print(x, y, xa, ya)
    elif y > 500:
        ya *= -1
        #print(x, y, xa, ya)
    elif y < 0:
        ya *= -1
        #print(x, y, xa, ya)


while True:
    #User input
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                pu = True
                pd = False
            elif event.key == K_DOWN:
                pd = True
                pu = False
        elif event.type == KEYUP:
            if event.key == K_UP:
                pu = False
            elif event.key == K_DOWN:
                pd = False
    if pd:
            py += 0.2
    if pu:
            py -= 0.2
    physics(playerPaddle, ball)
    screen.fill((255,255,255))
    playerPaddle = pygame.draw.rect(screen, (128, 0, 0), (485, py, 10, 140))
    ball = pygame.draw.circle(screen, (0, 0, 255), (x, y), 10)
    text = font.render('Score: ' + str(ps), True, (255,255,255), (0,0,0))
    text.get_rect().centery = screen.get_rect().centery - 170
    text.get_rect().centerx = screen.get_rect().centerx
    screen.blit(text, text.get_rect())
    time.sleep(d)
    if d:
        xa, ya = random.randint(1, 10000) / 10000, random.randint(1, 10000) / 10000
    d = 0
    x += xa
    y += ya
    pygame.display.flip()