''' the CAnny edge detector is an edge detection operator 
that uses a multistage algorithm to detect the wide range of 
edges in images
It was develop by John F.Canny in 1986

The Canny edge detection algorithm is compsed of 5 steps

1. Noise reduction 
 using gaussian filter to smoothen the image
2. Gradient calculation
 to find the intensity of the image
3. Non maximum supression
 to get rid of unwanted noise from the edge
4. Double threshold
to determine potential edges
5. Edge Tracking by Hysteresis
 to finalise the detection of the edgedby suppersiong all the other 
 edges which are not connected to potential edges
 
'''

import cv2 
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread('./data/messi5.jpg',0)
'''canny = cv2.Cann(source img, threshold1 ,threshold2 for Hysteresis)
'''
canny = cv2.Canny(img, 100,200)
titles=['img','canny']
images=[img,canny]

for i in range(2):
    plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()


