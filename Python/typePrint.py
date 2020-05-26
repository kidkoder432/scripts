def typePrint(val, speed):
    import time
    val = list(val)
    print()
    for letter in val:
        print(letter, end = ' ')
        time.sleep(1)
    print('\n')
while True:
    val = input('Please enter a string of characters. >')
    speed = float(input('Please enter the timing between each letter. >'))
    typePrint(val, speed)
 