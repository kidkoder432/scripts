ragas = open('ragas.csv')
rindex = open('raga-index.txt', 'w')
for r in str(ragas.read()).split('\n'):
    print(r)
    if r:
        rindex.write(r.split(',')[0] + ': ' + r.split(',')[1] + ' ' + r.split(',')[2])
        rindex.write('\n')
ragas.close()
rindex.close()