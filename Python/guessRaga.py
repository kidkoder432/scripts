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

    if message == []:
        return 0.0 # No words at all, so return 0.0.
    while "'" in message:
        del message[message.index("'")]
    for i in range(len(message) - 2):
        for saptak in list(SAPTAKS.keys()):
            if ''.join(message[i:i + 2]) in saptak:
                SAPTAKS[saptak] += 1
    return SAPTAKS
while True:
    phrase = input('Enter a phrase and I will guess what raga it is in! >')
    SAPTAKS = getEnglishCount(phrase)
    high = 0
    for freq in list(SAPTAKS.values()):
        if freq > high:
            high = freq
    keys = list(SAPTAKS.keys())
    if high > 3:
        print("I'm most certain that it is %s." %(keys[list(SAPTAKS.values()).index(high)]))
    else:
        print("I'm not sure.")
