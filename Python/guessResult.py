f = open('someData.csv', 'w')
for i in range(1, 101):
    f.write('%s,%s,%s' %(i, i*2, i*4))
    f.write('\n')

f.close()
import pandas as pd
data = pd.read_csv('someData.csv')
data[:]