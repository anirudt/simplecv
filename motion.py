from SimpleCV import *

cam = Camera()

time.sleep(2)
print "First shot"
i1 = cam.getImage()

time.sleep(2)

print "Second shot"
i2 = cam.getImage()
time.sleep(2)

print "Third Shot"
i3 = cam.getImage()
time.sleep(2)

print "Showing motion shot"
i4 = (i1/4 + i2/2 + i3/4)
i4.save("motion.png")