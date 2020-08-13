def conv(phrase):
    t = 0
    multiplier = 10 ** (len(phrase) - 1)
    notes = ['','S','r','R','g','G','M','m','P','d','D','n','N']
    for n in phrase:
        t += notes.index(n) * multiplier
        multiplier /= 10
    return t

print('Phase 1: Generating data...')
import platform, os
from guessRaga import getRagas, loadDictionary
def isValid(phrase):
    for x in range(len(phrase) - 1):
        if phrase[x].lower() == phrase[x+1].lower() and ((phrase[x].islower() and phrase[x+1].isupper()) or (phrase[x].isupper() and phrase[x+1].islower())):
            return False
    return True
DATA = {}
threshold = 0.7
import itertools
phrases = []
print("Generating phrases...")
for i in range(5,6):
    for p in itertools.product(['S', 'r', 'R', 'g', 'G', 'M', 'm', 'P', 'd', 'D', 'n', 'N'], repeat=i):
        SAPTAKS = loadDictionary()
        print('Evaluating phrase: ' + ''.join(p))
    
        if isValid(''.join(p)):
            guesses = getRagas(SAPTAKS, p, threshold)
        if guesses and len(guesses.split(' or ')) == 1:
            DATA[p] = guesses
print('Writing data...')
f = open('data.csv', 'w+')
for k in list(DATA.keys()):
    f.write(''.join(k) + ', ' + DATA[k])
    f.write('\n')
f.close()
print('Done.')
print('Collected ' + str(len(DATA)) + ' entries')
for raga in list(SAPTAKS.keys()):
    print('Writing data...')
    fname = 'is' + raga[:raga.index(':')] + '.csv'
    f = open(fname, 'w+')
    for k in list(DATA.keys()):
        print(DATA[k], raga[:raga.index(':')])
        if raga[:raga.index(':')] in DATA[k]:
            f.write(str(conv(''.join(k))) + ', ' + '1')
        else:
            f.write(str(conv(''.join(k))) + ', ' + '0')
        f.write('\n')




    f.close()
    print('Done.')
    print('Collected ' + str(len(DATA)) + ' entries')
print('Finished operations.')