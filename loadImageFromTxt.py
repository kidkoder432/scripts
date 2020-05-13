from PIL import Image
from PIL.ImageDraw import *
import gzip, time, saveImageAsText
print('Loading image...')
f = gzip.open('imageBytes.txt', 'r')
content = f.read().decode('utf-8')
rows = content.split('        ')
im = Image.new('RGB', (len(rows[0].split('  ')) - 1 ,len(rows) - 1))
for y in range(len(rows) - 1):
    row = rows[y].split('  ')
    for x in range(len(row) - 1):
        col = row[x]
        col = list(col)
        print(col)
        try:
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
        print(67)
        print(col)
        im.putpixel((x, y), col)

    print('Finished row %s' %(y))
im.save(saveImageAsText.fname + '_MOD'+ '.bmp')
