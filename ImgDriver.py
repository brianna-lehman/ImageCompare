#!/usr/bin/python

import Image
import ImageChops
import os
import sys

def main():
	path = sys.argv[1]
	counter = 0
	images = os.listdir(path)

	for filenameA in images:
		imgA = Image.open(filenameA)

		for filenameB in images[1:]:
			imgB = Image.open(filenameB)

			diff = ImageChops.difference(imgA, imgB)

			if diff == 0:
				os.remove(path+imgB)
				counter += 1

	print(counter+" files deleted\n")

main()

# open a path from the command line
# for every jpeg image in the folder
	# open imageA
	# for every next image in the folder
		# open imageB

		# compare the two images

		# if imageA == imageB
			# delete imageB from the folder
			# counter++