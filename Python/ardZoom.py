import pyfirmata
import time, pyautogui
vc, ac = False, False
board = pyfirmata.Arduino('COM5')



board.digital[10].mode = pyfirmata.INPUT
board.digital[9].mode = pyfirmata.INPUT
while True:
    vs = board.digital[10].read()
    if vs:
        vc = not vc
        print('Video: %s' %(vc))