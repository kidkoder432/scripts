from PIL import Image
import gzip, time, saveImageAsText
f = gzip.open('imageBytes.txt', 'r')
content = f.read().decode('utf-8')
rows = content.split('        ')
im = Image.new('RGB', (len(rows[0].split('  ')) ,len(rows)))
for y in range(len(rows) - 1):
    row = rows[y].split('  ')
    for x in range(len(row)):
        col = row[x]
        col = list(col)
        del col[col.index('(')]
        del col[col.index(')')]
        del col[col.index(',')]
        del col[col.index(',')]
        col = ''.join(col)
        col = col.split(' ')
        for c in col:
            col.append(int(c))
        del col[:4]
        col = tuple(col)
        im.putpixel((x, y), col)
    print('Finished row %s' %(y))
im.save(saveImageAsText.path + '_MOD'+ '.bmp')
