import jiphy
jiphy.to.javascript('''import random, winsound, time, sys, keyboard

def playSeq():
    print('Welcome to SoundTest!')

    while True:
        ans = ''
        print('Would you like to learn how to play, or play the game?')
        ans = input()
        
        if ans.lower() == 'play':
            print('3...\n2...\n1...\nGO!')
            time.sleep(1)
            Hz = random.randint(300, 1000)
            winsound.Beep(Hz, 2000)
            userHz = random.randint(200, 1000)
            winsound.Beep(userHz, 2000)
            print('Press G to decrease the frequency, or press H to increase it. Then press Enter when you are finished.')
            while True:
                
                if keyboard.is_pressed('a'):
                    winsound.Beep(Hz, 500)
                    time.sleep(0.01)
                
                if keyboard.is_pressed('g'):
                    while keyboard.is_pressed('g'):
                        userHz -= 1
                        time.sleep(0.001)
                        winsound.Beep(userHz, 100)
                
                elif keyboard.is_pressed('h'):
                    while keyboard.is_pressed('h'):
                        userHz += 1
                        time.sleep(0.001)
                    winsound.Beep(userHz, 100)
                        
                
                else:
                    pass
                time.sleep(0.01)
                if keyboard.is_pressed('enter'):
                    break
                
                else:
                    pass

            if userHz in range(Hz - 15, Hz +15):
                print('Great job! You have a very sharp ear.')
                print('Standard frequency: %s\nYour frequency: %s' %(Hz, userHz)) 
            
            else:
                print('Looks like you need some more practice!')
                print('Standard frequency: %s\nYour frequency: %s' %(Hz, userHz)) 
            
        elif ans.lower() == 'learn' or 'how to play':
            print('The computer will beep at a random frequency. Then it will beep again at another frequency. You have to match the second frequency with the first one. ')



        print('Press Enter to quit, or press Space + Enter to play again.')
        x = input()
        if len(x) == 0:
            sys.exit()

        else:
            continue

playSeq()''')


