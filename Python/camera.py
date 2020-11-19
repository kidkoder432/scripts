import cv2, pygame
from pygame.locals import *
pygame.init()
scr = pygame.display.set_mode((1920,1080), pygame.RESIZABLE)
cam = cv2.VideoCapture(0)
cv2.namedWindow('test')

img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow('test', frame)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            cam.release()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                print("Escape hit, closing...")
                pygame.quit()
                cam.release()
                exit()
            elif event.key == K_SPACE:
                # SPACE pressed
                scr.fill((255, 255, 255))
                img_name = "opencv_frame_{}.png".format(img_counter)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                img_counter += 1
    pygame.display.flip()
cam.release()
