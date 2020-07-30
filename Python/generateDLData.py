print('Phase 1: Generating data...')
import platform, os
from guessRaga import getRagas, loadDictionary
DATA = {}
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
for i in range(5, 8):
    for p in itertools.product(['S', 'r', 'R', 'g', 'G', 'M', 'm', 'P', 'd', 'D', 'n', 'N'], repeat=i):
        SAPTAKS = loadDictionary()
        print('Evaluating phrase: ' + ''.join(p))
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
            f.write(''.join(k) + ', ' + '1')
        else:
            f.write(''.join(k) + ', ' + '0')
        f.write('\n')

    f.close()
    print('Done.')
    print('Collected ' + str(len(DATA)) + ' entries')
print('Finished operations.')
SAPTAKS = loadDictionary()
for raga in list(SAPTAKS.keys()):
    f = open('is'+ raga[:raga.index(':')]+'.csv')
    cont = str(f.read())
    f.close()
    for c in cont.split('\n'):
        print(c)
        c = c.split(', ')
        if c:
            f = open('is'+raga[:raga.index(':')]+'.csv', 'w')
            c[0] = str(conv(c[0]))
            f.write(', '.join(c))
            f.write('\n')
