
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
import itertools
phrases = []
i = 5
s = 0
print(i)
for p in itertools.product(['S', 'r', 'R', 'g', 'G', 'M', 'm', 'P', 'd', 'D', 'n', 'N'], repeat=i):
    for x in range(4):
        if p[x].lower() != p[x+1].lower():
            s += 1
    if s == 4:
        s = 0
        print(p)
        phrases.append(p)
for phrase in phrases:
    while "-" in phrase:
        del phrase[phrase.index("-")]
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
    guesses = '  '.join(guesses)