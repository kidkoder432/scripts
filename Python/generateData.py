print('Phase 1: Generating data...')
import platform, os
from guessRaga import getRagas, loadDictionary
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
for i in range(5,6):
    for p in itertools.product(['S', 'r', 'R', 'g', 'G', 'M', 'm', 'P', 'd', 'D', 'n', 'N'], repeat=i):
        SAPTAKS = loadDictionary()
        print('Evaluating phrase: ' + ''.join(p))
        guesses = getRagas(SAPTAKS, p, threshold)
        if guesses:
            DATA[p] = guesses
print('Writing data...')
f = open('data.csv', 'w+')
for k in list(DATA.keys()):
    f.write(''.join(k) + ', ' + DATA[k])
    f.write('\n')
f.close()
print('Done.')
print('Collected ' + str(len(DATA)) + ' entries')
# print('Phase 2: Updating index...')
# f = open('data.csv', 'r')
# fi = open('raga-index.txt')
# ALL_RAGAS = str(fi.read()).split('\n')
# fi.close()
# content = str(f.read())
# RAGA_INDEX = ALL_RAGAS
# content = content.split('\n')
# del content[-1]
# for r in content:
#     phrase = r.split(', ')[0]
#     ragas = r.split(', ')[1].split('/')
#     for raga in ragas:
#         for scale in ALL_RAGAS:
#             if raga == scale[:scale.index(':')]:
#                 RAGA_INDEX[ALL_RAGAS.index(scale)]  += (' ' + phrase)
# fi = open('saptaks.txt', 'w')
# for r in RAGA_INDEX:
#     print(len(r.split(' ')))
# print(len(''.join(RAGA_INDEX).split(' ')))
# fi.write('\n'.join(RAGA_INDEX))
# fi.close()
# print('Finished operations.')
# f.close()

