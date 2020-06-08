import cv2
import numpy as np


'''to get the coordinates of mouse,button etc
list out event from cv2 lib which contain EVENT'''
# event=[i for i in dir(cv2) if 'EVENT' in i]
# print(event)

# def click_event(event,x,y,flag,param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         print(x,', ' ,y)
#         font= cv2.FONT_HERSHEY_SIMPLEX
#         xy=str(x)+', '+str(y)
#         cv2.putText(img,xy,(x,y),font,1,(255,255,0),2)
#         cv2.imshow('image',img)  #this imshow will show the point on the image whwere mouse is clicked

#     if event == cv2.EVENT_RBUTTONDOWN:
#         print('right ',x,', ',y)
#         font = cv2.FONT_HERSHEY_SIMPLEX
#  1.   #    xy = str(x)+', '+str(y)
#  2.      blue=img[y,x,0]
#  2.       green=img[y,x,1]
#  2.      red=img[y,x,2]
#  2.      bgr = (str(blue) +','+str(green) +', '+str(red))
#  1.   #    cv2.putText(img,xy,(x,y),font,.5,(250,197,220),2)
#  2.       cv2.putText(img,bgr,(x,y),font,.5,(250,197,220),2)
#         cv2.imshow('image',img)

# img= cv2.imread('./data/lena.jpg')
# #img=np.zeros((512,512,3),np.uint8)
# cv2.imshow('image',img) # this imshow will initially show the blackscreen

# # this setMouseCallback is used to call the event function and control mouse
# cv2.setMouseCallback('image',click_event)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


'''draw a point and then connecting point to a line'''

# def click_event(event,x,y,flag,param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         cv2.circle(img,(x,y),3,(0,0,255),-1)
#         points.append((x,y))
#         if len(points)>=2:
#             cv2.line(img,points[-1],points[-2],(255,0,0),4)
#         cv2.imshow('image',img)

# img=np.zeros((512,512,3),np.uint8)
# cv2.imshow('image',img)
# points=[]

# cv2.setMouseCallback('image',click_event)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''program if we clicked at any point on a colored image then same co;or will be 
filled on the other window'''

def click_event(event,x,y,flag,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        cv2.circle(img,(x,y),3,(255,0,0),-1)
        mycolorimage=np.zeros((512,512,3),np.uint8)

        mycolorimage[:]=[blue,green,red]

        cv2.imshow('color',mycolorimage)

img= cv2.imread('./data/lena.jpg')
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
