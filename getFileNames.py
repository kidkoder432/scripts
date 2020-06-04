import os
fl = open('files.txt', 'w')
for r, d, f in os.walk('c:\\users\\findp'):
    for file in f:
        fl.append(os.path.join(r, file))

fl.close()