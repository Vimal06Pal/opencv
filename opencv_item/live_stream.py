import cv2
cap = cv2.VideoCapture(0)
# 0 for default camera
# 1,2,3... for other camera connected to system externaly
#if we want to read any video cap = cv2.VideoCapture('video.format')
while(True):
    ret,frame = cap.read()
    # read method will return true==> 1 if frame is available
    #if return 1 or 0 will be saved in cap variable and 
    # frame will be save in frame variable

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#    gray = cv2.cvtColor(source,conversion what we want to do)
    cv2.imshow('frame',gray)

    #cv2.imshow('name of the frame we want to give','frame variable')

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()