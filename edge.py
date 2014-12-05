from SimpleCV import *

cam = Camera()
disp = Display()

img = cam.getImage()
cat = img.edges(t1=10)
cat.save("Edge.png")
blobs = cat.findBlobs()
blobs.draw()
cat.save("Edge-blob.png")
print "Change incorporated"

blobs[-1].draw(color=Color.PUCE,width=-1,alpha=128)

cat.save("labelled.png")

if blobs: # if blobs are found
		circles = blobs.filter([b.isCircle(0.2) for b in blobs]) # filter out only circle shaped blobs
		if circles:
			img.drawCircle((circles[-1].x, circles[-1].y), circles[-1].radius(),SimpleCV.Color.BLUE,3) # draw the circle on the main image

img.save("circled.png")
print "Done"


