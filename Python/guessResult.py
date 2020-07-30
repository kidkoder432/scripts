import random
f = open('someData.txt', 'w')
for i in range(1, 1001):
    r = random.randint(1, 100)
    if r < 90:
        m = 4
    else:
        m = random.random()
    f.write('%s,%s,%s' %(i, i*2, i*m))
    f.write('\n')

f.close()

import pandas as pd
data = pd.read_csv('someData.csv')
x = data[:, :-1]
y = data[:, -1]
