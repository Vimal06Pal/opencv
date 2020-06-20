''' 
Background subtraction (BS) is a common and widely used 
technique for generating a foreground mask 
(namely, a binary image containing the pixels belonging 
to moving objects in the scene) by using static cameras.

As the name suggests, BS calculates the foreground mask 
performing a subtraction between the current frame and 
a background model, containing the static part of the 
scene or, more in general, everything that can be considered
 as background given the characteristics of the observed scene.
'''

import cv2 
import numpy as np

cap = cv2.VideoCapture('./data/vtest.avi')
# cap = cv2.VideoCapture(0)

# fgpa = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
fgpa = cv2.createBackgroundSubtractorKNN(detectShadows=False)
while True:
    ret, frame = cap.read()
    if frame is None: 
        break
    fgmask = fgpa.apply(frame)

    cv2.imshow('frame',frame)
    cv2.imshow('FG MASK FRAME',fgmask) 


    keybord = cv2.waitKey(30)
    if keybord == 'q' or keybord == 27:
        break
cap.release()
cv2.destroyAllWindows()