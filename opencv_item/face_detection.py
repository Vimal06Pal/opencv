import cv2
face_cascade = cv2.CascadeClassifier('./data/Haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./data/Haarcascades/haarcascade_eye.xml')
# print(face_cascade)
img = cv2.imread('./data/Modi.jpg')
img = cv2.resize(img,(512,512))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 5)
eyes = eye_cascade.detectMultiScale(gray, 1.1, 5)
'''
objects = cv2.CascadeClassifier.detectMultiScale(image,ScaleFactor,
                            MinNeighbours)

image = Matrix of the type cv_8U containing an image where objects
are detected.

objects = vector of rectangles where each rectangle contains the detected object,
the rectangle may be partially outside the original image.

scaleFactor = Parameter specifiying how much the image
size is reduced at each image scale

minNeighbours = Parameter specifying how many neighbours each candidate
rectangle should have to retain it.

'''
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
for (xe,ye,we,he) in  eyes:
    cv2.rectangle(img,(xe,ye),(xe+we,ye+he),(255,0,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)