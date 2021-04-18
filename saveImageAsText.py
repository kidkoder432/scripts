from PIL import Image
import gzip
import os, time

path = input(
    "Enter the file path of the images. For example: C:\\Users\\findp\\Pictures > "
)
os.chdir(path)
fname = input(
    "Which file would you like to open? Note: can only be in " + os.getcwd() + " > "
)
now = time.time()
im = Image.open(fname)
w, h = im.size
f = gzip.open("imageBytes.txt", "wt")
# f.write('Image data for ' + fname)
for y in range(h):
    f.write(".")
    for x in range(w):
        f.write(",")
        f.write(" ".join([str(x) for x in im.getpixel((x, y))]))
    # print("Finished row %s" % (y + 1), "out of", h)
    print(y/h * 100, '\b% complete', end='\b\b\b\b\b\b\b\b\r')
    # end = time.time()
    # print("Time: %s" % (end - now))
f.close()
