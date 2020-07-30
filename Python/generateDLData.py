print('Phase 1: Generating data...')
import platform, os
from guessRaga import getRagas, loadDictionary
DATA = {}
def isValid(phrase):
    for x in range(len(phrase) - 1):
        if phrase[x].lower() == phrase[x+1].lower():
            return False
    return True
def conv(phrase):
    t = 0
    multiplier = 10 ** (len(phrase) - 1)
    notes = ['','S','r','R','g','G','M','m','P','d','D','n','N']
    for n in phrase:
        t += notes.index(n) * multiplier
        multiplier /= 10
    return t
import itertools
phrases = []
print("Generating and evaluatiing phrases...")
for i in range(5, 6):
    for p in itertools.product(['S', 'r', 'R', 'g', 'G', 'M', 'm', 'P', 'd', 'D', 'n', 'N'], repeat=i):
        SAPTAKS = loadDictionary()
        print('Evaluating phrase: ' + ''.join(p))
        if not isValid(p):
            continue    
        guesses = getRagas(SAPTAKS, ''.join(p), 0.72, '/')
        if guesses:
            DATA[p] = guesses
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
