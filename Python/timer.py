from time import sleep
import os
frequency = 880
time = int(input('How many seconds to count down?'))
print(time)
dur = 1
for i in range(time * 10):
    print('Time left: %s' %((time - i)), end='\r')
    os.system('play -n --no-show-progress synth %s sin %s' % (dur / 2, frequency))
    sleep(dur / 2)
    dur /= 1.01
