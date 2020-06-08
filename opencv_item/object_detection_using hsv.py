'''
H = Hue => hue corresponds to the color component(base pigment), hense just 
    selecting a range of Hue you can select any color. (0 - 360)

S = SAturation ==> it is the amount of color (depth of the pigment)(dominance of Hue)
   (0- 100%)

V = value ==> it is the brightness of the color. (0 - 100%).

'''
import cv2
import numpy as np 

def nothing(x):
    pass

while (1):
    frame = cv2.imread('./data/smarties.png')

    cv2.imshow('frame',frame)

    key == cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()