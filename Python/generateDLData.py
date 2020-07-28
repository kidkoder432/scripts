print('Phase 1: Generating data...')
import platform, os
from guessRaga import getRagas
def isRaga(phrase, raga):
	if raga.lower() in getRagas(phrase, 0.72, '/').lower():
		return True
	else:
		return False
DATA = {}
threshold = 0.7
import itertools
phrases = []
print("Generating phrases...")
for i in range(5, 8):
    for p in itertools.product(['S', 'r', 'R', 'g', 'G', 'M', 'm', 'P', 'd', 'D', 'n', 'N'], repeat=i):
        phrases.append(p)
f = open('raga-index.txt')
c = str(f.read())
f.close()
print("Evaluating phrases...")
for raga in c.split('\n'):
    for phrase in phrases:
        print('Evaluating phrase: ' + ''.join(phrase))
        guesses = isRaga(phrase, raga[:raga.index(': ')])
        if guesses:
            DATA[phrase] = '1'
        else:
            DATA[phrase] = '0'
    print('Writing data...')
    f = open('is%s.csv', 'w+' % (raga[:raga.index(': ')]))
    for k in list(DATA.keys()):
        f.write(''.join(k) + ', ' + DATA[k])
        f.write('\n')
    f.close()
    print('Done.')
    print('Collected ' + str(len(DATA)) + ' entries')
print('Finished operations.')