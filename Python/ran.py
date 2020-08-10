
import random
while True:
    number1 = random.randint(1, 6)
    number2 = random.randint(1, 6)
    print('First roll: ' + str(number1))
    print('Second roll: ' + str(number2)) 
    print('Total: ' + str(number1 + number2))
    print('Press Enter to roll again.')
    input()
    
        
