''' An image gradient is a directional change in the 
intensity or color in an image

it is the building block of the imge preprocessing  
image gradient is used to find edges in an image

methods in image gradient
Laplacian 
sobel x 
sobel y
''' 
import cv2 
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread('./data/sudoku.png',cv2.IMREAD_GRAYSCALE)

'''lapacian(source img ,datatype)
cv2.CV_64F is the data type which converted in 64 bit float
it support the negative number which we will be dealing with 
when laplacian methed is applied on our img
At last we take the absolute value of lap and converted into unsigned 
int8
'''
lap = cv2.Laplacian(img,cv2.CV_64F,ksize=3)
lap = np.uint8(np.absolute(lap))

''' sobelx
sobelx = cv2.Sobel(img,cv2.CV_64F,order of x derivative ,order of y deribvative)
sobely = cv2.Sobel(img,cv2.CV_64F,,order of x derivative,order of y deribvative)
'''
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1)

sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))


'''cobining result using bitwise or operator 
'''
sobelCombine = cv2.bitwise_or(sobelx,sobely)

titles = ['images','laplacian','sobelx','sobely','sobelCombine']
images = [img,lap,sobelx,sobely,sobelCombine]

for i in range(5):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()