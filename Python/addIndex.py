ragas = open('ragas.csv')
rindex = open('raga-index.txt', w)
for r in str(ragas.read()).split('\n'):
    rindex.write(r.split(',')[0] + ': ' + r.split(',')[1] + ' '  r.split(',')[2])

