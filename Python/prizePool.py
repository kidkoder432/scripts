prizePool = 1
import random
print('Welcome to Prize Pool!')
print('''How to play:
1. I'll flip a coin.
2. If the coin lands heads, the prize pool doubles.
3. If the coin lands tails, the game ends, and you get all the money in the prize pool.''')
coin = 1
while coin != 0:
    print('Press Enter to flip the coin!')
    input()
    coin = random.randint(0, 1)
    print('Yay! The prize pool doubles!')
    prizePool *= 2
print('Game Over! You won $%s!' % (prizePool)) 
