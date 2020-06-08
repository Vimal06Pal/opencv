'''
H = Hue => hue corresponds to the color component(base pigment), hense just 
    selecting a range of Hue you can select any color. (0 - 360)

S = SAturation ==> it is the amount of color (depth of the pigment)(dominance of Hue)
   (0- 100%)

V = value ==> it is the brightness of the color. (0 - 100%).

'''
import cv2
import numpy as np 

def nothing(x):
    pass

cap = cv2.VideoCapture(0)   # for video

cv2.namedWindow('tracking')
# creating trackbar lower hue,lower saturation, lower value
cv2.createTrackbar('LH','tracking',0,255, nothing)
cv2.createTrackbar('LS','tracking',0,255, nothing)
cv2.createTrackbar('LV','tracking',0,255, nothing)

# creating trackbar for upper hue, upper saturation, upper value
cv2.createTrackbar('UH','tracking',255,255, nothing)
cv2.createTrackbar('US','tracking',255,255, nothing)
cv2.createTrackbar('UV','tracking',255,255, nothing)

while (1):
#    frame = cv2.imread('./data/smarties.png')  # for  image
    ret, frame = cap.read()  # for video

    hsv= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    l_h =cv2.getTrackbarPos('LH','tracking')
    l_s =cv2.getTrackbarPos('LS','tracking')
    l_v =cv2.getTrackbarPos('LV','tracking')

    u_h =cv2.getTrackbarPos('UH','tracking')
    u_s =cv2.getTrackbarPos('US','tracking')
    u_v =cv2.getTrackbarPos('UV','tracking')

    # next two line will make the color combination array
    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv , l_b, u_b)

    res = cv2.bitwise_and(frame, frame, mask=mask)

     

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()            # for video
cv2.destroyAllWindows()