

import time
while True:
    val = input('Please enter a string of characters. >')
    speed = float(input('Please enter the timing between each letter. >'))
    val = list(val)
    print()
    for letter in val:
        print('\r' + letter)
        time.sleep(speed)
    print('\n')