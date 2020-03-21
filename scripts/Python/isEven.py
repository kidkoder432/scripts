result = 0
def isEven(number):
    result = number % 2 
    if result == 1:
        print('This number is odd.')
    else:
        print('This number is even.')
    return None 
while True:
    print('Enter a number.')
    number = int(input())
    isEven(number)
        
        
