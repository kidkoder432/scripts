print('Phase 1: Generating data...')
import platform, os
from guessRaga import getRagas, loadDictionary
DATA = {}
import itertools
phrases = []
print("Generating and evaluatiing phrases...")
for i in range(5, 6):
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