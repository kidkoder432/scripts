from PIL import Image
import os, random
SIZE = (100, 100)
path = input('Enter the save location for the random image > ')
os.chdir(path)
fname = input('Enter the file name > ')
im = Image.new(SIZE, 'RGB')
for w in range(SIZE[0]):
    for h in range(SIZE[1]):
        im.putpixel((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
print('Image created.')
im.save(fname)
print('Stored in directory: %s' %(path))
