import cv2
# reading image from file
img = cv2.imread("./data/Lena.jpg",1)
# print(img)
cv2.imshow('image',img)
k=cv2.waitKey(0) & 0xFF

# if k== Esc
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
# write an image  in a file
    cv2.imwrite('./ lena_copy.png',img)
    cv2.destroyAllWindows() 