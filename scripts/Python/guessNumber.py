# this is a guess the number game.
import random
print('Hello. What is your name?')
name = input()
while True:
    print('Well, ' + name + ', I am thinking of a number between 1 and 100. Take a guess.')
    secretNumber = random.randint(1, 100)
    for guessesTaken in range(1, 9):
        guess = int(input())
        if guess < secretNumber:
            print('Too low.')
        elif guess > secretNumber:
            print('Too high.')
        else:
            break
        print('Take another guess.')

    if guess == secretNumber:
        print('Good job, ' + name + '. You guessed my number in ' + str(guessesTaken) + ' guesses!')
    else:
        print('You did not guess my number. It was ' + str(secretNumber) + '.')

    print('If you want to play again, press Enter.')
    input()
        
