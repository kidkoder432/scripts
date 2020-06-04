from PIL import Image
from PIL.ImageDraw import *
import gzip, time, saveImageAsText#, pyperclip
print('Loading image...')
f = gzip.open('imageBytes.txt', 'r')
content = f.read().decode('utf-8')
#pyperclip.copy(content)
rows = content.split('        ')
im = Image.new('RGB', (len(rows[1].split('  ')),len(rows) - 1))
for y in range(1, len(rows) - 1):
    row = rows[y].split('  ')
    for x in range(1, len(row)):
        col = row[x]
        col = list(col)
        del col[col.index('(')]
        del col[col.index(')')]
        del col[col.index(',')]
        del col[col.index(',')]
        col = ''.join(col)
        col = col.split(' ')
        for c in range(3):
            col.append(int(col[c]))
        del col[:3]
        col = tuple(col)
        im.putpixel((x - 1, y - 1), col)
    print('Finished row %s' %(y))
im.save(saveImageAsText.fname + '_MOD'+ '.jpg')