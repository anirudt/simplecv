'''
This script studies the Palette extraction. This can be used widely in ML
for color classification requirements. 

'''
import math

from SimpleCV import *

cam = Camera()
disp = Display()

img = cam.getImage()
p = img.getPalette(bins=11)

i=Image("simplecv")

pal = img.rePalette(p)
temp = img.drawPaletteColors()

result = pal.sideBySide(temp, side="bottom")
result.save("palette.png")
print p


'''
After this, the first 2-3 arrays of the p list
could be tested for a particular colour, for detecting
some particular color. Also, the learning of the color epsilon 
can be done via using some test datasets generated.
'''
