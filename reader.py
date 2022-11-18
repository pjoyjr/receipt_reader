import cv2
from os import walk as os_walk
from pathlib import Path

from PIL import Image
import PIL.Image

from pytesseract import image_to_string
import pytesseract

# List all the files and directories
path = Path(__file__).parent / 'fake_receipts'
for (root, directories, files) in os_walk(path, topdown=False):
	for name in files:
		# Read the image
		print(Path(root)/name)
		image = cv2.imread(str(Path(root)/ name))		
		# imS = cv2.resize(image, (1350, 1150))
		cv2.imshow("output",image)
		# cv2.imwrite('Output Image.PNG', image)
		cv2.waitKey(0)
		# Extracting text from the document
		pytesseract.pytesseract.tesseract_cmd = r"C:\Users\pjoyj\AppData\Local\Tesseract-OCR\tesseract.exe"
		output = pytesseract.image_to_string(image, lang='eng')
		print(output)
		input()

	# for name in directories:
	# 	print(Path(root)/ name)