from SimpleCV import *

def main():
	
	cam = Camera()
	disp = Display()

	while disp.isNotDone():
		print "We are looping"
		img = cam.getImage()
		if disp.mouseLeft:
			print "We will break"
			break
		img.save(disp)


