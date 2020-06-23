import cv2 
# making object of CascadeClassifier
face_cascade = cv2.CascadeClassifier('./data/Haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./data/Haarcascades/haarcascade_eye.xml')

#reading the video from webcam
cap = cv2.VideoCapture(0)
while cap.isOpened():
    _, img = cap.read()
    # img = cv2.resize(img,(512,512))
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)                 #coverting img into GrayScale
    faces = face_cascade.detectMultiScale(gray,1.1,4)           # detecting face from the image
    eyes = eye_cascade.detectMultiScale(gray, 1.1, 4)           # detecting eyes from the frame

    #making the rectangle by looping through point given by ascade.detectMultiScale

    # for face
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
        track = x,y,w,h
    
    # For eyes
    for (xe,ye,we,he) in  eyes:
        cv2.rectangle(img,(xe,ye),(xe+we,ye+he),(255,0,0),2)

    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()