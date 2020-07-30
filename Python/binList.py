binList = []
import random, time
for i in range(100):
    #time.sleep(0.001)
    binum = random.randint(0, 1)
    binList.append(str(binum))
print(''.join(binList))
