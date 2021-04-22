import gzip  # , pyperclip
import time

from PIL import Image

import saveImageAsText

now = time.time()
print("Loading image...")
f = gzip.open("imageBytes.txt", "r")
content = f.read().decode("utf-8")
# pyperclip.copy(content)
rows = content.split(".")
im = Image.new("RGB", (len(rows[1].split(",")), len(rows) - 1))
for y in range(1, len(rows) - 1):
    row = rows[y].split(",")
    for x in range(1, len(row)):
        col = row[x]
        col = tuple([int(s) for s in col.split(" ")])
        im.putpixel((x - 1, y - 1), col)
    # print("Finished row %s" % (y))
    print(y / len(rows) - 1 * 100, '%% complete', end='\r')
    # end = time.time()
    # print("Time taken: %s" % (end - now))
im.save(saveImageAsText.fname + "_MOD" + ".jpg")
