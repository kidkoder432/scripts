import turtle
import random
turtle.colormode(1.0)
while True:
    #print('Enter the RGB value of any color and this program will show you the inverse of it.')
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    print('The RGB value is %s, %s, %s.' % (red, green, blue))
    red /= 255
    green /= 255
    blue /= 255

    turtle.bgcolor(red, green, blue)

    import time
    time.sleep(2)

    wRed = 1
    wGreen = 1
    wBlue = 1
    iRed = wRed - red
    iGreen = wGreen - green
    iBlue = wBlue - blue
    iColor = (iRed, iGreen, iBlue)
    turtle.bgcolor(iColor)
    print('The inverse RGB value is %s, %s, %s.' % (round(iRed * 255), round(iGreen * 255), round(iBlue * 255)))
    print()
    time.sleep(2)
    
