print('Phase 1: Generating data...')
import platform, os
DATA = {}
threshold = 0.7
from guessRaga import getRagas
import itertools
phrases = []
print("Generating phrases...")
for i in range(5, 7):
	for p in itertools.product(['S', 'r', 'R', 'g', 'G', 'M', 'm', 'P', 'd', 'D', 'n', 'N'], repeat=i):
		phrases.append(p)
print("Evaluating phrases...")
for phrase in phrases:
	print('Evaluating phrase: ' + ''.join(phrase))
	guesses = getRagas(phrase, '/')
	if guesses:
		DATA[phrase] = guesses
print('Writing data...')
f = open('data.csv', 'w')
for k in list(DATA.keys()):
	f.write(''.join(k) + ', ' + DATA[k])
	f.write('\n')
f.close()
print('Done.')
print('Collected ' + str(len(DATA)) + ' entries')
print('Phase 2: Updating index...')
f = open('data.csv', 'r')
fi = open('raga-index.txt')
ALL_RAGAS = str(fi.read()).split('\n')
fi.close()
content = str(f.read())
RAGA_INDEX = ALL_RAGAS
content = content.split('\n')
del content[-1]
for r in content:
	phrase = r.split(', ')[0]
	ragas = r.split(', ')[1].split('/')
	for raga in ragas:
		print(raga)
		for scale in ALL_RAGAS:
			if raga == scale[:scale.index(':')]:
				RAGA_INDEX[ALL_RAGAS.index(scale)]  += (' ' + phrase)
fi = open('saptaks.txt', 'w')
for r in RAGA_INDEX:
	print(len(r.split(' ')))
print(len(''.join(RAGA_INDEX).split(' ')))
fi.write('\n'.join(RAGA_INDEX))
fi.close()
print('Finished operations.')
f.close()

# print('Phase 3: Finding patterns...')
# print('Reading data...')
# f = open('data.csv')
# c = []
# r = []
# for i in str(f.read()).split('\n'):
# 	c.append(i.split(', ')[0])
# 	r.append(i.split(', ')[1])
# f.close()
# print('Generating patterns...')
# patterns = []
# p = []
# for phrase in c:
# 	for i in range(2, len(phrase) + 1):
# 		for x in range(len(phrase) - (i - 1)):
# 			p.append(phrase[x:i + x])
# 	print(p)
# 	patterns.append(p)
# 	p = []	
# for p in range(len(patterns)):
# 	c[p] = patterns[p]
# print('Writing data...')
# f = open('data.csv', 'w')
# for i in range(len(r)):
# 	print('Data being written: ' + ', '.join(c[i]) + ', ' + r[i])
# 	f.write(', '.join(c[i]) + ', ' + r[i])
# 	f.write('\n')
# f.close()
# print('done')

