def into():
    from SimpleCV import Shell
    Shell.main()


def go():
    from SimpleCV import *   
    cam = Camera()
    
    while(1):
        print "Inside the loop"
	img = cam.getImage()
        img.show()
    
