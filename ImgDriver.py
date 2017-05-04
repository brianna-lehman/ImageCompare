#!/usr/bin/python

from PIL import Image
from PIL import ImageChops
import os
import sys

def main():
	path = sys.argv[1]
	print(path)
	counter = 0
	images = os.listdir(path)

	for filenameA in images[0:-2]:
		imgA = Image.open(path+"/"+filenameA)

		for filenameB in images[1:]:
			imgB = Image.open(path+"/"+filenameB)

			diff = ImageChops.difference(imgA, imgB)

			if diff == 0:
				os.remove(path+"/"+imgB)
				counter += 1

	print counter, "files deleted\n"

main()
