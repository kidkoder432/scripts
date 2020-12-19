from threading import Thread
print('Phase 1: Generating data...')
def f1():
    # d1 = {}
    for p in x[0]:
        if isValid(p):
            guesses = getRagas(p, threshold)
        if guesses:
            d1[p] = guesses
    
def f1():
    d1 = {}
    for p in x[0]:
        if isValid(p):
            guesses = getRagas(p, threshold)
        if guesses:
            d1[p] = guesses
def f1():
    d1 = {}
    for p in x[0]:
        if isValid(p):
            guesses = getRagas(p, threshold)
        if guesses:
            d1[p] = guesses
from guessRaga import getRagas, loadDictionary
def isValid(phrase):
    for x in range(len(phrase) - 1):
        if phrase[x].lower() == phrase[x+1].lower() and ((phrase[x].islower() and phrase[x+1].isupper()) or (phrase[x].isupper() and phrase[x+1].islower())):
            return False
    return True

threshold = 0.7
import itertools
phrases = []
print("Generating phrases...")
l = list(itertools.product(list('SRGMPDNrgmdn'), repeat=5))  
n = len(l) / 3
x = [l[i:i + n] for i in range(0, len(l), n)]  
print('Writing data...')
f = open('data.csv', 'w+')
for k in list(DATA.keys()):
    f.write(''.join(k) + ', ' + DATA[k])
    f.write('\n')
f.close()
print('Done.')
print('Collected ' + str(len(DATA)) + ' entries')
# for raga in list(SAPTAKS.keys()):
#     print('Writing data...')
#     fname = 'is' + raga[:raga.index(':')] + '.csv'
#     f = open(fname, 'w+')
#     for k in list(DATA.keys()):
#         print(DATA[k], raga[:raga.index(':')])
#         if raga[:raga.index(':')] in DATA[k]:
#             f.write(str(conv(''.join(k))) + ', ' + '1')
#         else:
#             f.write(str(conv(''.join(k))) + ', ' + '0')
#         f.write('\n')
#     f.close()
#     print('Done.')
#     print('Collected ' + str(len(DATA)) + ' entries')
# print('Finished operations.')