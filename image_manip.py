'''

This script is just to study the 
basics of colour manipulations.

Pretty self explanatory.

'''


from SimpleCV import *

def main():

	img = Image("simplecv")
	

	#Playing with Scaling
	thumbnail = img.scale(90,90)
	thumbnail = thumbnail.show()

	#Playing with erosion
	eroded = img.erode()
	eroded.show()

	#Effect of cropping
	cropped = img.crop()
	cropped.show()

	