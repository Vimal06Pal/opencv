'''
histogram as a graph or plot which gives the overall
idea of intensity distribution of image/graph

we can draw the histogram using
1. matplotlib
2. cv2.calHist
'''

import cv2 
import numpy as np 
import matplotlib.pyplot as plt


# # black imge of 200x200 
# img = np.zeros((200,200), np.uint8)
# cv2.rectangle(img,(0,100),(200,200),(255),-1)
# cv2.rectangle(img,(0,50),(100,100),(127),-1)


# cv2.imshow("img",img)
# # argument = (source img.ravel(), max value.[range])
# plt.hist(img.ravel(),256,[0,256])
# plt.show()


# cv2.waitKey(0)
# cv2.destroyAllWindows()

''' working on images in grayscale mode'''
# img = cv2.imread('./lena_copy.png',0)

# cv2.imshow('img',img)
# plt.hist(img.ravel(),256,[0,256])
# plt.show()

# cv2.waitKey()
# cv2.destroyAllWindows( )  

'''' working with color img'''

# img = cv2.imread('./lena_copy.png')
# b,g,r = cv2.split(img)

# cv2.imshow('img',img)
# cv2.imshow('b',b)
# cv2.imshow('g',g)
# cv2.imshow('r',r)


# plt.hist(b.ravel(),256,[0,256])
# plt.hist(g.ravel(),256,[0,256])
# plt.hist(r.ravel(),256,[0,256])

# plt.show()

# cv2.waitKey(0)
# cv2.destroyAllWindows()

''' histogram using  cv2.calHist() method'''

img = cv2.imread('./lena_copy.png',0)
cv2.imshow('img',img)
# arguments([src image],[channel],[mask],[hist size or max value],[range])
hist = cv2.calcHist([img] ,[0],None, [256],[0,256])
plt.plot(hist)

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
