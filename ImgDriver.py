import Image, ImageChops
import sys

def main():
	path = sys.argv[1]
	counter = 0

	for filename in os.listdir(path):
		imgA = Image.open(filename)

# open a path from the command line
# for every jpeg image in the folder
	# open imageA
	# for every next image in the folder
		# open imageB

		# compare the two images

		# if imageA == imageB
			# delete imageB from the folder
			# counter++