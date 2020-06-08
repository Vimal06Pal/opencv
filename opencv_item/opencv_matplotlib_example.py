import cv2 
import matplotlib.pyplot as plt

# img = cv2.imread('./lena_copy.png')

# cv2.imshow('img',img)

# # to convert img in rgb mode so that plt give the same result
# '''operncv (b,r,g)
# matplotlib (r,g,b)'''

# img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# plt.imshow(img)
# # to remove x and y scale 
# plt.xticks([]),plt.yticks([])
# plt.show()

# cv2.waitKey(0)
# cv2.destroyAllWindows()

''' showing thresholding techniw=que in one frame using subplot'''

img = cv2.imread('./data/sudoku.png')

_, th1 = cv2.threshold(img,123,255,cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img,123,255,cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img,123,255,cv2.THRESH_TOZERO)
_, th4 = cv2.threshold(img,123,255,cv2.THRESH_TOZERO_INV)
_, th5 = cv2.threshold(img,123,255,cv2.THRESH_TRUNC)

titles =['original','THRESH_BINARY','THRESH_BINARY_INV','THRESH_TOZERO','THRESH_TOZERO_INV','THRESH_TRUNC']
images = [img,th1,th2,th3,th4,th5]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])


plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()




