UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'

def loadDictionary():
    dictionaryFile = open('python\\saptaks.txt')
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        englishWords[word] = 0
    dictionaryFile.close()
    return englishWords

SAPTAKS = loadDictionary()

def getEnglishCount(message):
    message = list(message)

    if message == []:
        return 0.0 # No words at all, so return 0.0.
    while "'" in message:
        del message[message.index("'")]
    for saptak in list(SAPTAKS.keys()):
        for i in range(len(message) - 1):
            if ''.join(message[i:i + 1]) in saptak:
                SAPTAKS[saptak] += 1
    return SAPTAKS
while True:
    phrase = input('Enter a phrase and I will guess what raga it is in! >')
    getEnglishCount(phrase)
    print(SAPTAKS)
    high = 0
    for freq in list(SAPTAKS.values()):
        if freq > high:
            high = freq
    keys = list(SAPTAKS.keys())
    print("I'm most certain that it is %s." %(keys[list(SAPTAKS.values()).index(high)]))

