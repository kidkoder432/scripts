import os
try:
    from PIL import Image
except:
	import Image
import pytesseract
ch = input('Enter the directory the file is in (or "here" for this directory: ')
if ch != 'here':
	os.chdir(ch)
print(pytesseract.image_to_string(Image.open(input('Enter filename: '))))

