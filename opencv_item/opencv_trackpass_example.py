''' trackpass is useful when we want to change the value at run time'''
import cv2
import numpy as np 


# #creating call back function
# def nothing(x):
#     print(x)


# # create black image, a window
# img = np.zeros((300,512,3),np.uint8)
# #img = cv2.imread('./lena_copy.png',1)
# cv2.namedWindow('image')

# # creating trackbar
# # cv2.createTrackbar(trackbarName,windowname,min value,high value,callback function)
# cv2.createTrackbar('B', 'image', 0, 255, nothing)
# cv2.createTrackbar('G', 'image', 0, 255, nothing)
# cv2.createTrackbar('R', 'image', 0, 255, nothing)

# # if we add switch to control trackbar
# switch = '0 : OFF\n 1 : ON'
# cv2.createTrackbar(switch, 'image', 0, 1, nothing)

# while 1:
#     cv2.imshow('image',img)
#     k = cv2.waitKey(1) & 0xFF 
#     if k == 27:
#         break
    
#     # get the trackbar value 
#     #arguments (name of the trackbar,window of the trackbar)
#     b = cv2.getTrackbarPos('B','image')
#     g = cv2.getTrackbarPos('G','image')
#     r = cv2.getTrackbarPos('R','image') 
#     s = cv2.getTrackbarPos(switch,'image')

#     if s == 0:
#         img[:] = np.zeros((300,512,3),np.uint8)

#     else:
#         img[:] = [b,g,r]
# cv2.destroyAllWindows()

'''
2nd example

in this example we have to create a trackbar and get its current position and 
show it position on the image
image can be toggle by switch in color and gray scale form
'''


# #creating call back function
def nothing(x):
    print(x)
# img =cv2.imshow('image',img)
cv2.namedWindow('image')

cv2.createTrackbar('CP', 'image', 10, 400, nothing)

switch = 'color/gray'

cv2.createTrackbar(switch, 'image', 0, 1, nothing)

while(1):
    img = cv2.imread('./lena_copy.png')
    pos = cv2.getTrackbarPos('CP','image')
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,str(pos),(50,150),font,4,(85,175,129),3)

    k= cv2.waitKey(1) & 0xFF
    if k ==27:
        break

    s = cv2.getTrackbarPos(switch,'image')

    if s == 0:
        pass
    else:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    img = cv2.imshow('image',img)

cv2.destroyAllWindows()


