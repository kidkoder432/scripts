import pyautogui 
x = input('Press Enter after you move the mouse to the place I should click. > ')
c = pyautogui.position()
while True: 
    pyautogui.click(c) 
