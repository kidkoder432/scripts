import random, winsound, time, keyboard

print('Welcome to SoundTest!')


def getDifficulty(m):
    d = int(input("Select a difficulty: 1 is easiest and 10 is hardest. "))

    if m.lower().startswith('m'):
        listenAgain = False
    else:
        listenAgain = True
        d = int(d * 3/10) + 7
        
    if d > 10: d = 10
    if d < 1: d = 1
    t = ((10 - d)*2)
    return listenAgain, t

while True:
    ans = ''
    print('Would you like to learn how to play, or play the game?')
    ans = input()
    if ans.lower() == 'play':
        m = input('Select game mode: (M)emory or (A)ccuracy: ')
        listenAgain, t = getDifficulty(m)
        print('3...\n2...\n1...\nGO!')
        time.sleep(1)
        Hz = random.randint(300, 1000)
        winsound.Beep(Hz, 2000)
        time.sleep(0.03)
        userHz = random.randint(200, 1000)
        winsound.Beep(userHz, 2000)
        if listenAgain:
            print('Press G to decrease the frequency, or press H to increase it. Press A if you would like to hear the first sound again. Then press Enter when you are finished.')
        else:
            print('Press G to decrease the frequency, or press H to increase it. Then press Enter when you are finished.')

        while True:
            if listenAgain:
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

        if userHz in range(Hz - t, Hz + t + 1):
            print('Great job! You have a very sharp ear.')
            print('Standard frequency: %s\nYour frequency: %s' %(Hz, userHz)) 
        else:
            print('Looks like you need some more practice!')
            print('Standard frequency: %s\nYour frequency: %s' %(Hz, userHz)) 
        
    elif ans.lower() == 'learn' or 'how to play':
        print('''The computer will beep at a random frequency. Then it will beep again at another frequency. You have to match the second frequency with the first one. ''')



    print('Press Enter to quit, or press Space + Enter to play again.')
    x = input()
    if len(x) == 0:
        break    
    else:
        continue

