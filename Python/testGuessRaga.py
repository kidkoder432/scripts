def loadDictionary():
    dictionaryFile = open('saptaks.txt')
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
def tri(n):
    t = 0
    for i in range(n):
        t += i
    return t
import random, itertools
print('Welcome To Guess Raga Test!')
print('Follow the prompts. Hit CTRL-C to save and quit.')
phrases = [p for p in itertools.product(list('SRGMPDNrgmdn'), repeat=6)]
nt, npt = [True, True]
f = open('log.csv')
nt = 'Phrase, Computer Guesses, User Guesses' not in str(f.read())
npt = 'Phrases tested' not in str(f.read())
phrasesTested = len(str(f.read()).split('\n')) - 1
f.close()
f = open('log.csv', 'a')
if nt:
    f.write('Phrase, Computer Guesses, User Guesses')
correct = 0
threshold = 0.3
try:
    while phrasesTested < 1000:
        phrase=list(random.choice(phrases))
        print('Phrase # %s: ' + ''.join(phrase) %(phrasesTested + 1))
        if not input('Is this phrase valid? > ').lower().startswith('y'):
            phrase = []
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
            accuracy = SAPTAKS[guess] / tri(len(phrase))
            if accuracy >= threshold:
                guesses.append(guess[:guess.index(':')])
        if guesses:
            print('I think your phrase is a ' + ' or '.join(guesses) + ' phrase.')
            userGuesses = input('Which ragas is it really in? Enter your guesses seperated by "&" > ')
            for g in userGuesses.split('&'):
                if g in guesses:
                    correct += 1
                    break

        else:
            print('I\'m not sure which raga your phrase is in.')
            userGuesses = input('Which ragas is it really in? Enter your guesses seperated by "&" > ')
        f.write('\n')
        f.write(''.join(phrase) + ', ' + '/'.join(guesses) + ', ' + '/'.join(userGuesses.split('&')))
        phrasesTested += 1
        phrase = []
except KeyboardInterrupt:
    print('Saving progress...')
    f.close()
