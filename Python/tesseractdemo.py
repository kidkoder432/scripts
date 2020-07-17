try:
    from PIL import Image
except:
	import Image
import pytesseract
print(pytesseract.image_to_string(Image.open(input('Enter file to open: '))))

