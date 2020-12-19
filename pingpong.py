import pygame, random, time
from pygame.locals import *
pygame.init()
intelligence = random.randint(1, 100)
d = 0
py = 0
ps, cs = 0, 0
pu, pd = False, False
x = 250
y = 250
cy = 0
screen = pygame.display.set_mode([500, 500])
playerPaddle = pygame.draw.rect(screen, (128, 0, 0), (485, py, 10, 140))
computerPaddle = pygame.draw.rect(screen, (128, 0, 0), (5, 0, 10, 140))
ball = pygame.draw.circle(screen, (0, 0, 255), (x, y), 10)
font = pygame.font.SysFont(None, 30)
xa, ya = [(random.randint(0, 6000) - 3000) / 10000] * 2

def physics(p, b, c):

    t = 100
    global x, y, xa, ya, ps, cs, d, intelligence
    if x < t:
        if 99 < x < 100:
            intelligence = random.randint(1, 100)
        if intelligence < 80:
            c.centery = y
        else:
            pass
    
    if b.colliderect(c):
        xa = abs(xa)
        x = 26
        t = 25
    
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
    #Clear screen
    physics(playerPaddle, ball, computerPaddle)

    screen.fill((255,255,255))
    playerPaddle = pygame.draw.rect(screen, (128, 0, 0), (485, py, 10, 140))
    computerPaddle = pygame.draw.rect(screen, (128, 0, 0), (5, computerPaddle.centery - 70, 10, 140))
    ball = pygame.draw.circle(screen, (0, 0, 255), (x, y), 10)
    text = font.render('Score: ' + str(ps), True, (255,255,255), (0,0,0))
    text.get_rect().centery = screen.get_rect().centery - 170
    text.get_rect().centerx = screen.get_rect().centerx
    screen.blit(text, text.get_rect())


    #draw objects

    pygame.display.flip()
    if d:
        time.sleep(d)
        xa, ya = [(random.randint(0, 6000) - 3000) / 10000] * 2
    d = 0
    x += xa
    y += ya
    