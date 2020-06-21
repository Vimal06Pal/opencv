''' Harris corner Detector

1. It determines which window produce very large 
variations in intensity when moved in both x and y dirction

2. With each such window found, a score R is computes

3. After applying a threshold to this score important 
corners are selected & marked.
-------------------------------------------

It determines which window produce very large 
variations in intensity when moved in both x and y dirction

E(u,v) =   E   w(x,y)   |I(x+u , y+v) - I(x,y)|^2
         (x,y)         <- for corner this difference is very large->    
 
w(x,y)                 window fn (the centre is located at x,y)
I(x+u , y+v)           shifted intensity(if window is shifed u,v in x,y direction respesctively)
I(x,y)                 intensity

we have to maximise this equn using taylor exapansion 
we get:-
        E(u,v) = [u  v] M [u]
                          [v]   

M = E w(x,y)[IxIx   IxIy]
    x,y     [IxIy   IyIy]                       E= summation
   
   Ix and Iy are the derivatives of x and y respectively


2. With each such window found, a score R is computed

R= det(M)-k(trace(M))^2

where
. det(M)==lambda1.lambda2
. trace(M) = lambda1 + lambda2
. lambda1(/\) and lambda2(/\) are the eigen values of M

After applying a threshold to this score important 
corners are selected & marked.

(i) |R| is small, which happens when /\1 and /\2 are small, 
 the region is flat

(ii) R<0, which happens when /\1>>/\2 or vise versa, 
the region is edge
                                    (\  )     (\  )
(iii) R is large, which happens when(/\1) and (/\2 )are large 
and /\1 ~ /\2, the region is a corner.


'''

import cv2 
import numpy as np 

img = cv2.imread('./data/chessboard.png')
img = cv2.resize(img,(512,512)) 
cv2.imshow('img',img)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)  # cornerHarris take the gray image into float32 format
'''img - input img,it should be grayscale and float32 type
block size - it is the size of neighbourhood considered for corner detection
ksize - Aperture parameter of Sobel derivative used
k - Harris detected free parameter in the equation

'''
dst = cv2.dilate(dst,None) # dilated the corner of the image

img[dst > 0.01 * dst.max()] = [0,0,255] # marking the optimal threshold value on dilated img corner and put the color on the corner

cv2.imshow('dst',img)

if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()