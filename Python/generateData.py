
import platform, os
DATA = {}
os.chdir('python')

def loadDictionary():
    dictionaryFile = open("saptaks.txt")
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
import itertools
phrases = []
i = 5
print("Generating phrases...")
for p in itertools.product(['S', 'r', 'R', 'g', 'G', 'M', 'm', 'P', 'd', 'D', 'n', 'N'], repeat=i):
    phrases.append(p)
print("Evaluating phrases...")
for phrase in phrases:
    print('Evaluating phrase: ' + ''.join(phrase))
    SAPTAKS = getEnglishCount(phrase)
    high = 0
    guesses = []
    for freq in list(SAPTAKS.values()):
        if freq > high:
            high = freq
    keys = list(SAPTAKS.keys())
    for i in keys:
        guess = i
        if SAPTAKS[guess] >= high and high >= 7:
            guesses.append(guess[:guess.index(':')])
    guesses = '  '.join(guesses)
    if guesses:
        DATA[phrase] = guesses
print('Writing data...')
f = open('data.csv', 'w')
for k in list(DATA.keys()):
    f.write(''.join(k) + ', ' + DATA[k])
    f.write('\n')
f.close()
print('Done.')
print('Collected ' + str(len(DATA)) + ' entries')