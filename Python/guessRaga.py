# Guess The Raga Program - By Prajwal Agrawal
# This program CANNOT be run from an external program; it MUST be run by changing 
# directories to here and then being run.

import platform
if platform.system() == 'Windows':
    f = 'python\\saptaks.txt'
else:
    f = 'Python/saptaks.txt'

def loadDictionary():
    dictionaryFile = open(f)
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        englishWords[word] = 0
    dictionaryFile.close()
    return englishWords

def getEnglishCount(message):
    SAPTAKS = loadDictionary()
    message = list(message)
    while "'" in message:
        del message[message.index("'")]
    for x in range(2, len(message)):
        for i in range(len(message) - x):
            for saptak in list(SAPTAKS.keys()):
                if ''.join(message[i:i + x]) in saptak:
                    SAPTAKS[saptak] += 1             
    return SAPTAKS

while True:
    phrase = input('Enter a phrase and I will guess what raga it is in! >')
    SAPTAKS = getEnglishCount(phrase)
    high = 0
    guesses = []
    for freq in list(SAPTAKS.values()):
        if freq > high:
            high = freq
    keys = list(SAPTAKS.keys())
    for i in keys:
        guess = i
        if SAPTAKS[guess] >= high:
            guesses.append(guess[:guess.index(':')])
    bg = dg = 0 # how many times the program thinks Bhoopali and how many times it thinks Deshkar.
    if 'Bhoopali' and 'Deshkar' in guesses:
        for nt in list(phrase):
            if nt in ['P', 'D', 'S']:
                dg += 1
            else:
                bg += 1
        if bg > dg:
            del guesses[guesses.index('Deshkar')]
        elif dg > bg:
            del guesses[guesses.index('Bhoopali')]
    guesses = ' or '.join(guesses)
    if high > 5:
        print("I'm most certain that it is %s." %(guesses))
    else:
        print("I'm not sure.")