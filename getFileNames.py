import os, time
# ext = input('Which file extension would you like to search for? > ')
# folder = input('Which directory should I search? > ')
# save = input('Where should I save the file? > ')
fl = open('c:\\users\\findp\\files.txt', 'w')
# fl.write('Files ending with %s in %s\n\n' %(ext, folder))
for r, d, f in os.walk('c:\\users\\findp'):
    for file in f:
        print(os.path.join(r, file) + '\n')
        fl.write(os.path.join(r, file) + ' ')
fl.close()




f = open('c:\\users\\findp\\files.txt')
for file in f.read().split(' '):
    try:
        fl = open(file)
        print(file)
        print(fl.read())
        input('Next? ')
    except:
    print('Error on file %s' %(file)) 
    