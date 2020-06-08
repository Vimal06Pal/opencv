''' it is used when we use images of different 
resolution or size
eg:- searching a face in an image 

  level 0       blur and sub sample    level 1
original image -------------------->   1/2 resolution -------

level 1         blur and sub sample     level 2
1/2 resolution -------------------->    1/4 resolution

level 2         blur and sub sample     level 3
1/4 resolution -------------------->    1/8 resolution

level 3         blur and sub sample     level 4
1/8 resolution -------------------->    1/16 resolution

2 types of pyramid

1. Gaussian pyramid --. repeat filtering and sub sampling of an image
            (i). pyr down
            (ii). pyr up
2. Laplacian pyramid

'''

import cv2 
img = cv2.imread('./lena_copy.png')

# lower_resolution1 = cv2.pyrDown(img)
# lower_resolution2 = cv2.pyrDown(lower_resolution1)

# higher_resolution1 = cv2.pyrUp(lower_resolution2)

# cv2.imshow('original_image',img)
# cv2.imshow('lower_resolution1',lower_resolution1)
# cv2.imshow('lower_resolution2',lower_resolution2)

# cv2.imshow('higher_resolution2',higher_resolution1)
# cv2.waitKey(0)

# cv2.destroyAllWindows()

''' using loops'''
# layer = img.copy()


# for i in range(6):
#     layer = cv2.pyrDown(layer)

#     cv2.imshow(str(i),layer)

# cv2.imshow('higher_resolution2',img  )
# cv2.waitKey(0)

# cv2.destroyAllWindows()

''' Laplacian pyramid  no build in
 function is available for laplacian pyramid
 
 A levrl in Laplacian Pyramid is formed by the 
 difference between the level in Gaussian pyramid
  and expended version of its upper level in 
  Gaussian pyramid.'''

layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    # cv2.imshow(str(i),layer)

layer =gp[-1]
cv2.imshow('upper level Gaussian Pyramid',layer)
lp=[layer]

for i in range(5,0,-1):
  gaussian_extended = cv2.pyrUp(gp[i])
  laplacian = cv2.subtract(gp[i-1], gaussian_extended)
  cv2.imshow(str(i),laplacian)


cv2.imshow
cv2.imshow('higher_resolution2',img  )
cv2.waitKey(0)

cv2.destroyAllWindows()