import random, winsound, time, sys, keyboard
def playSeq():
    global userHz
    global Hz
    print('3...\n2...\n1...\nGO!')
    Hz = random.randint(300, 1000)
    winsound.Beep(Hz, 2000)
    userHz = random.randint(300, 1000)
    winsound.Beep(userHz, 2000)
    print('Press G to decrease the frequency, or press H to increase it. Then press Enter when you are finished.')
    while True:
        time.sleep(0.01)
        if keyboard.is_pressed('g'):
            while keyboard.is_pressed('g'):
                userHz -= 1
                winsound.Beep(userHz, 100)
        elif keyboard.is_pressed('h'):
             while keyboard.is_pressed('h'):
                 userHz += 1
                 winsound.Beep(userHz, 100)
             
        else:
            pass
        time.sleep(0.01)
        if keyboard.is_pressed('enter'):
            break
        else:
            pass
        
print('Welcome to SoundTest!')
while True:
    ans = ''
    print('Would you like to learn how to play, or play the game?')
    ans = input()
    if ans.lower() == 'play':
        playSeq()
        if userHz in range(Hz - 15, Hz +15):
            print('Great job! You have a very sharp ear.')
        else:
            print('Looks like you need some more practice!')
            print('Standard frequency: %s\nYour frequency: %s' %(Hz, userHz)) 
        
    elif ans.lower() == 'learn' or 'how to play':
        print(''' ''')



    print('Press Enter to quit, or press Space + Enter to play again.')
    x = input()
    if len(x) == 0:
        sys.exit()
    else:
        continue