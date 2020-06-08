import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread('./data/messi5.jpg')
grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
template = cv2.imread('./data/messi_face.jpg',0)
w,h = template.shape[::-1]
res = cv2.matchTemplate(grey,template, cv2.TM_CCOEFF_NORMED)
''' res will give the matrix , the point where the 
template matches there will be the maximum value will be noted 
else other places almost equal pattern is follwed'''
print(res)

threshold = 0.9  # guessing a threshold value to compare the original image 
loc = np.where(res >= threshold)  # get the location where template matches the original image
print(loc)
''' now we have to put the rectangle on the img of same size of the template
we use the loop because it wiil be good if more than on time template is matched'''
for pt in zip(*loc[::-1]):
    cv2.rectangle(img,pt, (pt[0]+w,pt[1]+h),(0,0,255),2)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()