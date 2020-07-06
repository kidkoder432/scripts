from PIL import Image
import os, secrets
random = secrets.SystemRandom()
SIZE = (1000, 1000)
path = input('Enter the save location for the random image > ')
if path:
    os.chdir(path)
fname = input('Enter the file name > ')
im = Image.new('RGB', SIZE)
for w in range(SIZE[0]):
    for h in range(SIZE[1]):
        im.putpixel((w, h), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
print('Image created.')
im.save(fname)
print('Stored in directory: %s' %(path))
