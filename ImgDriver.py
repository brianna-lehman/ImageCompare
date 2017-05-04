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
	i = 0

	while i < len(images)-1:
		j = i + 1
		
		filenameA = images[i]
		print "Compare ", filenameA

		imgA = Image.open(path+"/"+filenameA)

		while j < len(images):
			filenameB = images[i+1]
			print "to ", filenameB

			imgB = Image.open(path+"/"+filenameB)

			diff = ImageChops.difference(imgA, imgB)

			if diff == 0:
				os.remove(path+"/"+imgB)
				counter += 1

			j += 1
		i += 1

	print counter, "files deleted\n"

main()
