import numpy as np 
import cv2 

img = cv2.imread('./data/shapes.png')
img= cv2.resize(img,(512,512))
imgrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(imgrey,240,255,cv2.THRESH_BINARY)
contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    cv2.drawContours(img,[approx],0, (0,0,0),5)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    if len(approx) == 3:
        cv2.putText(img,'Triangle',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
    elif len(approx) == 4:
        x,y,w,h = cv2.boundingRect(approx)
        aspect_ratio = float(w)/h
        if aspect_ratio >= 0.95 and aspect_ratio <=1.05:
            cv2.putText(img,'rectangle',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
        else:
            cv2.putText(img,'rectangle',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
    elif len(approx) == 5:
        cv2.putText(img,'pantagon',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
    elif len(approx) == 10:
        cv2.putText(img,'star',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
    else:
        cv2.putText(img,'circle',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
cv2.imshow('shapes',img)

cv2.waitKey(0)
cv2.destroyAllWindows()