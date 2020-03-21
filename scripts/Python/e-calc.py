import math
import time
def eCalc(repeat):
    x = 0
    z = 0
    global y
    y = 0
    for i in range(repeat):
        z = 1 / math.factorial(x)
        x = x + 1
        y = z + y
        
while True:
    print('Please enter a number.')
    val = input()
    eCalc(int(val))
  #  print('The value of e is ' + str(y))
    print(y)
            
