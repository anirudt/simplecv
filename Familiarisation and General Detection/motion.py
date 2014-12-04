'''

This script can be made tp make a motion
blur with 3 images taken 10 seconds apart from time, 
which can be made to give a ghouly look!

Just kiddin'

Though it can look scary at times..
'''



from SimpleCV import *

cam = Camera()

time.sleep(5)
print "First shot"
i1 = cam.getImage()

time.sleep(10)

print "Second shot"
i2 = cam.getImage()
time.sleep(10)

print "Third Shot"
i3 = cam.getImage()
time.sleep(10)

print "Showing motion shot"
i4 = (i1/3 + i2/3 + i3/4)
i4.save("motion.png")