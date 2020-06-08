'''thresholding  is a very important segment technique 
used to seperate the object from its backgroung 
it require to compare the each pixel from the predefined 
threshold value]
it divide the imge into two part 
1. pixel contain  value less than threshold value
2. pixel contain value more than threshold value  
'''
 
import cv2
import numpy as np 

# img = cv2.imread('./data/gradient.png',0)
# # cv2.threshold(sourc img, threshold value, max value, type)
# _, th1 = cv2.threshold(img, 127,255,cv2.THRESH_BINARY)
# _, th2 = cv2.threshold(img, 56,255,cv2.THRESH_TRUNC)
# _, th3 = cv2.threshold(img, 56,255,cv2.THRESH_TOZERO)
# _, th4 = cv2.threshold(img, 56,255,cv2.THRESH_TRIANGLE)
# ''' in TRUNC method the color will remain same after 
# the threshold is achieved and before threshold obtained
# it will be similar as the original image'''

# ''' value < THRESH_TOZERO ==> ZERO ie black 
#      value > THRESH_TOZERO  ==>  same as image
#      '''
# cv2.imshow('image',img)
# cv2.imshow('th1',th1)
# cv2.imshow('th2',th2)
# cv2.imshow('th3',th3)
# cv2.imshow('th4',th4)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''adaptive threshoding technique
it is used where threshold value is calculated in smaller region''' 

img = cv2.imread('./data/sudoku.png')

_, th1 = cv2.threshold(img,123,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img, 25,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

cv2.imshow('img',img)
# cv2.imshow('th1',th1)
cv2.imshow('th2',th2)
 
cv2.waitKey(0)
cv2.destroyAllWindows()

