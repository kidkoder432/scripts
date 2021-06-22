from PIL import Image
import os, secrets

SIZE = (256, 256)
from itertools import product
colors = [x for x in product(list(range(256)), repeat=2)]
path = input('Enter the save location for the random image > ')
print(len(colors))
print(colors[0:256])
if path:
    os.chdir(path)
for i in range(256):
    im = Image.new('RGB', SIZE)
    fname = str(i) + '.jpg' #input('Enter the file name > ')
    for c in colors:
        im.putpixel(c, c + tuple([i]))
    print('Image created.')
    im.save(fname)
    print('Stored in directory %s with name %s' %(path, fname))
