import cv2
# cap = cv2.VideoCapture('./data/vtest.avi')
# cap = cv2.VideoCapture(0)

# while (cap.isOpened()):
#     ret,frame = cap.read()
#      # to get the property of the video
#     print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#     print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#     gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     cv2.imshow('frame',gray)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()

# #video writer>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# cap = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# # to save video in the location
# out = cv2.VideoWriter('./output/out.avi',fourcc,20.0,(640,480))

# while (cap.isOpened()):
#     ret,frame = cap.read()
#     # if we get the frame then we can write the frame in the out variable which store the location
#     # and format of the video
#     if ret == True:
#          # to get the property of the video
#         print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#         print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#         out.write(frame)

#         gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#         cv2.imshow('frame',gray)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

# cap.release()
# out.release()
# cv2.destroyAllWindows()

# cp.set()>>>set property>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import datetime # module to put date and time
cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3,720) # 3 for width and 480 is width size
cap.set(4,700) # 4 for height and 720 is height

print(cap.get(3))
print(cap.get(4))
while (cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
    #    gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        font=cv2.FONT_HERSHEY_SCRIPT_COMPLEX
        datet=str(datetime.datetime.now())
        text = 'Width: '+ str(cap.get(3)) + ' height: '+ str(cap.get(4))
    #    img=cv2.putText(frame,(str(cap.get(3))+str(cap.get(4))),(10,50),font,2,(239,147,197),2)
        img=cv2.putText(frame,text,(5,50),font,1,(239,147,197),2)
        img=cv2.putText(frame,datet,(30,450),font,1,(239,147,197),2,cv2.LINE_AA)

        cv2.imshow('frame',frame)
        

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break 

cap.release()
cv2.destroyAllWindows()  



