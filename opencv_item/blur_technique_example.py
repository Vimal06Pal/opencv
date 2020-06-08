'''smoothenig and blurring is the mosst commonly used 
operation is used on image pre processing
it is used to remove noise from the image
there are various FILTER WHICH ARE USED 
1.linear filter which are easy to used and  fast to achive result
2. Homogenous filter
    it is the most simple filter, each output pixel is the 
    mean of its kernel neighbors
3. Gaussian filter

4. Median filter
5. Bilateral filter

>>>>kernel formula (k) = 1/25(5 by 5 matrix)

>>> As in one-dimensional signals, images also can be filtered
with various low pass filter(LPF), high pass filter(HPF) etc

LPF helps in removing noises,bluring the images

HPF helps in finding edges in the images

'''
import cv2 
import matplotlib.pyplot as plt 
import numpy as np 

# img =cv2.imread('./data/download.jpg')
img =cv2.imread('./data/lena.jpg')

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

kernel =np.ones((5,5),np.float32)/25

dst = cv2.filter2D(img, -1, kernel)
'''cv2.filter(source image, desired dept,kernel)'''

''' blur function'''
blur = cv2.blur(img,(5,5))

''' gaussian filter is nothing but using different-weight-kernel, in both x and
 y direction
    -   [1  4  6  4 1]  -
    |   [4 16 24 16 4]  |
1/16|   [6 24 36 24 6]  |
    |   [4 16 24 16 4]  |
    |-  [1  4  6  4 1]  - 
 
 pixel located in the centre has the higher weight 
 weight of the pixel dec as the distance inc from the centre
 '''
gblur = cv2.GaussianBlur(img,(5,5),0)

''' median filter is something that replace each pixel's value 
with the median of its neighboring pixels. This method is great
when dealing with "salt and pepper noise".  

Salt-and-pepper noise is a form of noise sometimes seen on images. It is also known as impulse noise. This noise can be caused by sharp and sudden disturbances in the image signal. 
It presents itself as sparsely occurring white and black pixels.

image is available at .data/Noise_salt_and_pepper.png
'''
median = cv2.medianBlur(img, 5)
'''
median = cv2.medianBlur(src img, kernel size :- it should be odd 1 for real img)
'''
''' bileteral is mainly used to preserved border of the image  '''

bileteral = cv2.bilateralFilter(img,9,75,75)
titles = ['image','2d convolution','blur','Gaussianblur',
'median blur','bileteral']
images = [img,dst,blur,gblur,median,bileteral]

for i in range(6): 
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

