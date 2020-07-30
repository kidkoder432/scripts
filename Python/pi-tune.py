import winsound, time
pi = list('314159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196')
for n in pi:
    n = int(n)
    print(n, end = '')
    if n == 1:
        winsound.Beep(262, 500)
    elif n == 2:
        winsound.Beep(293, 500)        
    elif n == 3:
        winsound.Beep(330, 500)
    elif n == 4:
        winsound.Beep(349, 500)
    elif n == 5:
        winsound.Beep(392, 500)
    elif n == 6:
        winsound.Beep(440, 500)
    elif n == 7:
        winsound.Beep(494, 500)
    elif n == 8:
        winsound.Beep(523, 500)
    elif n == 9:
        winsound.Beep(587, 500)
    else:
        winsound.Beep(247, 500)
    #time.sleep(0.5)
