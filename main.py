import cv2
from PIL import Image
import pytesseract

im_file= "data/rg.jpg"

im = Image.open(im_file)
# out = im.transpose(Image.FLIP_TOP_BOTTOM)
# out.save("data/teste.jpg")
im = im.convert("1")
im.save("data/teste.jpg")
# im.show()
ocr_result = pytesseract.image_to_string(im)


print(ocr_result)
