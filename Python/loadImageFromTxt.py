from PIL import Image
import gzip
f = gzip.open('imageBytes.txt', 'r')
content = f.read().decode('utf-8')
content = content.split('        ')
im = Image.new('RGB', (len(content), len(content[0].split('  '))))
for y in range(len(content)):
    try:
        column = content[y].split('  ')
        for col in column:
            print(col)
            x = column.index(col) 
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
            print(col)
            while type(col[0]) != int:
                del col[0]
            col = tuple(col)
            im.putpixel((x, y), col)
    except:
        im.show()
