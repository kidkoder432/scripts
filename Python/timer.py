from time import sleep
import os
frequency = 880
time = int(input('How many seconds to count down?'))
print(time)
for i in range(time * 1000):
    print('Time left: %s' %((time * 1000 - i) / 1000), end='\r')
    #os.system('play -n --no-show-progress synth %s sin %s' % ((time * 1000 - i) / 1000, frequency))
    sleep((time * 1000 - i) / 1000)