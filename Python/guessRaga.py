def tri(n): #triangular number calculator
    t = 0
    for i in range(n):
        t += i
    return t
def loadDictionary(): # open raga database
    dictionaryFile = open("raga-index.txt")
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        englishWords[word] = 0
    dictionaryFile.close()
    return englishWords    
def getRagas(data, message, threshold=0.5, joiner=' or '): # guessing code
    SAPTAKS = data
    for x in range(2, 7):
        for i in range(len(message) - x + 1):
            for saptak in list(SAPTAKS.keys()):
                if ''.join(message[i:i + x]) in saptak:
                    SAPTAKS[saptak] += 1
    high = 0 
    guesses = []           
    for freq in list(SAPTAKS.values()):
        if freq > high:
            high = freq
    keys = list(SAPTAKS.keys())
    for i in keys:
        guess = i
        if SAPTAKS[guess] / tri(len(message)) >= threshold:
            guesses.append(guess[:guess.index(':')])
    guesses = joiner.join(guesses)        
    return guesses

def main():   # main interface
    SAPTAKS = loadDictionary()
    phrase = input('Enter a phrase and I will guess what raga it is in! > ')  
    threshold = 0.4 # threshold at which guesser algorithm starts guessing ragas
    if len(phrase) == 0:
        return 'Your phrase is empty.'
    for note in phrase:
        if note not in 'SrRgGMmPdDnN- ':
            return 'Your phrase has a letter which is not a note. Please reenter your phrase.'
    while '-' in phrase:
        phrase.replace('-', '')
    if len(phrase) < 8:
        return 'Your phrase is too short. Please enter a longer phrase.'
    guesses = getRagas(SAPTAKS, phrase, threshold)
    if guesses:
        return 'I think your phrase is a ' + guesses + ' phrase.'
    else:
        return 'I\'m not sure which raga your phrase is in.'

if __name__ == '__main__':
    while True:
        main()