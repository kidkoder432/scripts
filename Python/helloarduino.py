import pyfirmata, pyautogui
import time

board = pyfirmata.Arduino('COM9')

it = pyfirmata.util.Iterator(board)
it.start()
board.digital[9].mode = pyfirmata.INPUT
board.digital[10].mode = pyfirmata.INPUT
l = False
while True:
    v =  board