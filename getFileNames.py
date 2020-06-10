import os
fl = open('c:\\users\\findp\\files.txt', 'w')
for r, d, f in os.walk('c:\\users\\findp'):
    for file in f:
        print(os.path.join(r, file) + '\n')
        fl.write(os.path.join(r, file) + '\n')

fl.close()