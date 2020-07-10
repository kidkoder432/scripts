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
    for x in range(2, len(message) + 1):
        for i in range(len(message) - x + 1):
            for saptak in list(SAPTAKS.keys()):
                if ''.join(message[i:i + x]) in saptak:
                    SAPTAKS[saptak] += 1             
    return SAPTAKS

while True:
    phrase = list(input('Enter a phrase and I will guess what raga it is in! >'))
    while "-" in phrase:
        del phrase[phrase.index("-")]
    if len(phrase) < 6:
        print('The phrase you entered is too short. Please enter a longer phrase.')
        continue
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
    guesses = ' or '.join(guesses)
    if high > 10:
        print("I think that the raga is %s." %(guesses))
    else:
        print("I'm not sure.")