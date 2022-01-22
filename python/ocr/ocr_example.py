from PIL import Image
import pytesseract

# tesseract binary needs to be installed and then you need to point to it
# https://stackoverflow.com/questions/46140485/tesseract-installation-in-windows
pytesseract.pytesseract.tesseract_cmd = r'c:/Program Files (x86)/Tesseract-OCR/tesseract'

# had tesseract an image and it will pull out any text that it can find
IMG_PATH = 'img_hello_world.JPG'
text = pytesseract.image_to_string(Image.open(IMG_PATH))
print(text)
