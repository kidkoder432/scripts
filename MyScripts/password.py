
import winsound
import time
attempts = 5
pause = 30
i = 0
while i < 5:
    attempts = attempts - 5
    while attempts < 5:
        print('Enter password.')
        password = input()
        if password == 'prajwal08':               #change the password here
            print('Access granted.')
            break
        else:
            print('Access denied.')
            attempts = attempts + 1
            print('You have ' + str(5 - attempts) + ' attempts left.') 
    i = i + 1
    if attempts >= 5:
        print('Try again in ' + str(pause) + ' seconds.')
        #time.sleep(pause)
        pause = pause**2
        if i >= 5:
            for k in range (100):
                winsound.Beep(880, 750)
                time.sleep(0.25)
            #add code here to text or call someone.
        else:
            pass
                              
    else:
        print('Good job. You cracked the code in ' + str(attempts) + ' attempts!')
        break #add the code to whatever you want to do, like an application.
    
    


