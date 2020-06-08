import cv2
import numpy as np 

# img =cv2.imread('./data/messi5.jpg')

# print(img.shape) #return atuple of rows,columns, and channel
# print(img.size)  # return total no of pixel is accessed
# print(img.dtype) # return image dtype is obtained

# b,g,r = cv2.split(img) # split image into b,g,r separately
# img = cv2.merge((b,g,r))
# cv2.imshow('imag',img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# roi is the region of interest suppose if we want to work on a specific location on any image eg face,wall,background etc
# then region of interest come into play 

''' we have to copy the ball from messi img and 
copy it to other location'''

#   status :- incompleted

# img =cv2.imread('./data/messi5.jpg')

# def click_event(event,x,y,flag,param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         cv2.circle(img,(x,y),3,(255,0,0),2,-1)
#         points.append((x,y))
#         if len(points)>2:
#             cv2.circle(img,(x,y),3,(255,0,0),2,-1)
#         #    point.append((x,y))
#         #    cv2.rectangle(img,points[-1],points[-2],(255,0,0),2)
#         #    cv2.imshow('image',img)
#             print('points:',points)
#             print('points:',type(points[0][0]))
#         if len(points)>4:
#             ball = img[points[0][0]:points[0][1],points[1][0]:points[1][1]]
#             print('ball',ball)
#             print('points:',len(points))
#             # img[points[2][0]:[2][1],[3][0]:[3][1]] = ball        
#             # cv2.imshow('img',img)
            
# cv2.imshow('image',img)

# point=[]

# cv2.setMouseCallback('image',click_event)
# cv2.waitKey(0)
# cv2.destroyAllWindows()          

'''direct done above program'''
# img =cv2.imread('./data/messi5.jpg')

# ball = img[280:340,330:390]
# img[273:333, 100:160] = ball



# cv2.imshow('image',img)

# cv2.waitKey(0) 
# cv2.destroyAllWindows()


'''add two images'''

# img = cv2.imread('./data/messi5.jpg') 
# imgage= cv2.imread('./data/opencv-logo.png')
# cv2.imshow('image',imgage)

''' 1. method >> to add two images we should equal the dimension of both images'''

# img = cv2.resize(img,(512,512))
# imgage = cv2.resize(imgage,(512,512))


# dst = cv2.add(img,imgage)
# cv2.imshow('image',dst)
# cv2.waitKey(0) 
# cv2.destroyAllWindows()



print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


''' 2 method >>  add image using addweighted()'''

''' arguments
1. src1 ==> first image
2. alpha ==> weight to the first img
3. src2 ==> second image
4. beta ==> weight to the second image
5. gamma ==> scalar added to each sum '''

# img = cv2.resize(img,(512,512))
# imgage = cv2.resize(imgage,(512,512))

# dst = cv2.addWeighted(img,.6,imgage,.4,0)
# cv2.imshow('image',dst)
# cv2.waitKey(0) 
# cv2.destroyAllWindows()

''' 3 method >> bitwise operation  
it is useful when we working with mask
mask is the binary image of pixel om=n which the operation is to be performed
'''
img1 = np.zeros((250,250,3),np.uint8)
img1 = cv2.rectangle(img1,(75,0),(175,100),(255,255,255),-1)
img2 = np.zeros((250,250,3),np.uint8)
img2 = cv2.rectangle(img2,(125,0),(250,250),(255,255,255),-1)

bitAnd = cv2.bitwise_and(img2,img1)

cv2.imshow('image',img2)
cv2.imshow('imag',img1)
cv2.imshow('bitand',bitAnd)
cv2.waitKey(0) 
cv2.destroyAllWindows()

