'''
Morphological transformation are some simple operation based 
on the image shape

morphological transformations are normally performed 
on binary images

2 thing required for morphological operation
1. original image
2. kernel 
kernel tells you how to change the value of any
given pixel by combining it with different amount of the
neighboring pixels 
'''
import numpy as np 
import matplotlib.pyplot as plt 
import cv2

# # reading image into grayscale
# img = cv2 .imread('./data/smarties.png',cv2.IMREAD_GRAYSCALE)

# # using threshold converted into binary image
# _, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

# title = ['image','mask']
# images = [img, mask]
# for i in range(2):
#     plt.subplot(1, 2, i+1), plt.imshow(images[i],'gray')
#     plt.title(title[i])
#     plt.xticks([]),plt.yticks([])

# plt.show()
# cv2.waitKey(0)

# cv2.destroyAllWindows()


''' by running above code  we get the masked binary image and
gray scale image
inmasked image there is some black dot on the ball
to remove those dots we use dilation
'''
# reading image into grayscale
# img = cv2.imread('./data/smarties.png',cv2.IMREAD_GRAYSCALE)

# # using threshold converted into binary image
# _, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

# kernel =np.ones((2,2),np.uint8)
# dilated = cv2.dilate(mask, kernel,iterations=2 )
# ''' kernel is simply a matrix which iterated 
# over the masked image no of times we have given'''

# title = ['image','mask','dilation']
# images = [img, mask,dilated]
# for i in range(3):
#     plt.subplot(1, 3, i+1), plt.imshow(images[i],'gray')
#     plt.title(title[i])
#     plt.xticks([]),plt.yticks([])

# plt.show()
# cv2.waitKey(0)

''' one problem occur while using dilate method i.e if we use kernel size
big then image can be distorted as kernel  treats all the
pixel of image  same upto the size of the kernal to remove black spot'''

''' erosion is opposite to dilation here black part increase at the boundary  
kernel size '''

# img = cv2.imread('./data/smarties.png',cv2.IMREAD_GRAYSCALE)

# # using threshold converted into binary image
# _, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

# kernel =np.ones((2,2),np.uint8)
# dilated = cv2.dilate(mask, kernel,iterations=2 )
# ''' kernel is simply a matrix which iterated 
# over the masked image no of times we have given'''

# erosion = cv2.erode(mask,kernel,iterations=2)

# title = ['image','mask','dilation','erosion']
# images = [img, mask,dilated,erosion]
# for i in range(4):
#     plt.subplot(1, 4, i+1), plt.imshow(images[i],'gray')
#     plt.title(title[i])
#     plt.xticks([]),plt.yticks([])

# plt.show()
# cv2.waitKey(0)

''' opening morphology is the errosion followed by dilation
closeing morphology  is the dilation followed by erosion 
morphological gradient is the difference b/w dilation and errosion
top hat = original image -  opening 
'''
img = cv2.imread('./data/smarties.png',cv2.IMREAD_GRAYSCALE)

# using threshold converted into binary image
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernel =np.ones((2,2),np.uint8)
dilated = cv2.dilate(mask, kernel,iterations=2 )
''' kernel is simply a matrix which iterated 
over the masked image no of times we have given'''

erosion = cv2.erode(mask,kernel,iterations=2)

opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
mg = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernel)
toh = cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernel)
title = ['image','mask','dilation','erosion','opening',
'closing','morphological gradient','tophat']
images = [img, mask,dilated,erosion,opening,closing,mg,toh]
for i in range(8):
    plt.subplot(4, 2, i+1), plt.imshow(images[i],'gray')
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])

plt.show()
cv2.waitKey(0)
