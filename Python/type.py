import pyautogui, time
#for i in range(100):
 #   t.append(str(i))
#t = ', '.join(t)
while True:   
    whatToType = input('Please enter a string of text to type: ')
    if input('Should I start typing?(y/n): ').lower().startswith('y'):
        time.sleep(5)
        print('Starting...')
        for l in list(whatToType):
            pyautogui.press(l)
            #time.sleep(0.05)
