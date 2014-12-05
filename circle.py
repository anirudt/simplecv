'''
This is used to implement circle detection. 

'''


from SimpleCV import *

cam = Camera()
disp = Display()



while disp.isNotDone():
	print "Detecting"
	img = cam.getImage().flipHorizontal()
	dist = img.colorDistance(Color.BLACK).dilate(2)
	segmented = dist.stretch(200,255)
	blobs = segmented.findBlobs()

	if blobs:
		circles = blobs.filter([b.isCircle(0.5) for b in blobs])
		if circles:
			img.drawCircle((circles[-1].x, circles[-1].y), circles[-1].radius(),SimpleCV.Color.BLUE,3) # draw the circle on the main image
			img.save("circle.png")
			break
	if disp.mouseLeft:
		print "We will break"
		break
print "Out of the loop"		




	

