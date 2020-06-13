import platform
if platform.system() == 'Windows':
    f = 'python\\saptaks.txt'
else:
    f = 'Python/saptaks.txt'

def indices(lst, element):
    result = []
    offset = -1
    while True:
        try:
            offset = lst.index(element, offset+1)
        except ValueError:
            return result
        result.append(offset)
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
    for freq in list(SAPTAKS.values()):
        if freq > high:
            high = freq
    keys = list(SAPTAKS.keys())
    guess = keys[list(SAPTAKS.values()).indices(SAPTAKS, high)][:keys[list(SAPTAKS.values()).index(high)].index(':')]
    
    if high > 6:
        print("I'm most certain that it is %s." %(guess))
    else:
        print("I'm not sure.")

