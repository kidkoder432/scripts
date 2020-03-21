print('How many cats do you have?')
cats = input()
try:
    if int(cats) >= 4:
        print('There are a lot of cats.')
    elif int(cats) < 0:
        print('Invalid input. You cannot enter negative numbers.') 
        
    else:
        print("There aren't that many cats.")
except ValueError:
    print('You did not enter a number.')
    
