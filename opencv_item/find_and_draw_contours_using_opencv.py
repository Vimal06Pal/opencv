import cv2
import numpy as np 

img = cv2.imread('./data/opencv-logo.png')
img= cv2.resize(img,(512,512))
imgray = cv2.imread('./data/opencv-logo.png',0 )
# print(img.shape)
imgray= cv2.resize(imgray,(512,512))
ret ,thresh = cv2.threshold(imgray,127,255,0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
''' contours is a python list of all the contours in the image.
each individual contour is a numpy array of (x,y) coordinates
of boundary points of the object

hierarchy is the vector which contain the information of the image topology we'll
discuss in the later videos'''
print("no of counter =" + str(len(contours)))
print(contours[0])
cv2.drawContours(img,contours,1,(187,125,0),3)
# -1 is used to draw all the contours
''' cv2..drawContours(src img, contours,contour no, color, thickness)'''
cv2.imshow('Image',img)
cv2. imshow('Imagray',imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()
