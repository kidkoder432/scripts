from PIL import Image
import gzip, time
f = gzip.open('imageBytes.txt', 'r')
content = f.read().decode('utf-8')
content = content.split('        ')
im = Image.new('RGB', (len(content), len(content[0].split('  '))))
try:
    for y in range(len(content)):
        column = content[y].split('  ')
        for col in column:
            x = column.index(col)
            print(col)
            print(column.index(col))
            print((x, y))
            time.sleep(0.1)
            col = list(col)
            try:
                del col[col.index('(')]
            except:
                pass
            try:
                del col[col.index(')')]
            except:
                pass
            for i in range(2):
                try:
                    del col[col.index(',')]
                except:
                    pass
            
            for c in ''.join(col).split(' '):
                col.append(int(c))
            while type(col[0]) != int:
                del col[0]
            col = tuple(col)
            im.putpixel((x, y), col)
except:
    im.save('image.png')
