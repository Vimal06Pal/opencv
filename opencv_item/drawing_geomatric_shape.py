import cv2

img = cv2.imread('./lena_copy.png',1)
# #draw line
# img = cv2.line(img,(0,0),(25,87),(255,0,0),3)
# # draw arrow line
# imgs = cv2.arrowedLine(img,(0,0),(265,265),(0,255,0),5)
# # draw rectangle
img = cv2.rectangle(img,(4,0),(230,236),(0,0,255),2)# in rectangle thickness== -1 then rectangle will be filled by color
# # draw circle
# img= cv2.circle(img,(447,63),62,(255,165,250),5)
# # for color combination go to rgb color picker
# #img on which image we want to draw line
# #(0,0) starting coordinate
# #(255,255) ending coordinate
# #(255,0,0) (rgb) color channel

# # text put on image
# font=cv2.FONT_HERSHEY_SCRIPT_COMPLEX # font which we want
# img= cv2.putText(img,'opencvs',(10,500),font,8,(239,147,197),5)
# #(img,'what we want to write',font,fontscale(how big),color,thickness)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows( )


#image building using numpy array>>>>>>>>>>>>>>>>>>>>>>>

# import numpy as np 
# img = np.zeros([240,240,3],np.uint8)
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
