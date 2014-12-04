from SimpleCV import *
cam = Camera()

print "Get ready"
time.sleep(5)
i = 0
fin = cam.getImage()/11

while i<=10:
	img = cam.getImage()
	fin = fin + img/11
	time.sleep(0.1)
	i=i+1
print "We are done"	

fin.save("person_motion.png")	