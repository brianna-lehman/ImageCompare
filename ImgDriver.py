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

		# check that filenameA is a .jpeg or .jpg

		imgA = Image.open(path+"/"+filenameA)

		while j < len(images):
			filenameB = images[j]
			print "\tto ", filenameB

			# check that filenameB is a .jpeg or .jpg

			imgB = Image.open(path+"/"+filenameB)

			diff = ImageChops.difference(imgA, imgB).getbbox() is None

			print "\tDifference: ", diff

			if diff:
				os.remove(path+"/"+filenameB)
				counter += 1
				images = os.listdir(path)

			j += 1

		i += 1

	print counter, "files deleted\n"

main()
