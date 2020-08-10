import os
os.chdir('c:\\users\\findp')
fl = open('files.txt', 'w')
for r, d, f in os.walk('c:\\users\\findp'):
    for file in f:
        fl.write(os.path.join(r, file) + '\n')

fl.close()