''' 
the hough transform is a popular technique to detect any shape,
if you can represent that shape in a mathematical form.
It can detect the shape even if it is broken or distorted a litle bit

Two types in representation of line 
1. cartian co-ordinates  y= mx+c
2. polar co-ordinates   xcos0 + ysin0 =r

          Representation of line in hough space 
y                                       c
|                                       |
|     /<---- y= mx+c                    |
|    /                                  |   
|   /                                   |   
|  / <--- slope = m                     |
| /                                     |_ _ _ _  (m, c)
|/                                      |       |
|   intercept                           |       |
|___________________________  x         |_______|_______________________ m 
   
       xy space                                 mc space 

in the mc space we can represent a line as a point 
it will be helpful to manage a line because  single point (mc space) 
is easy to manage then a line  (xy space) 

c                                       y
|                                       |
|     /<---- c = Xa(m) + Ya             |        
|    /                                  |   
|   /                                   |   
|  / <--- slope = -Xa                   |
| /                                     |_ _ _ _  (Xa, Ya)
|/                                      |       |
|   intercept =Ya                       |       |
|___________________________  m         |_______|_______________________ x 
   
       mc space                                 xy space 
        (line)                                    (point)  


In Polar coordinate system 

r= x.cos0 + y.sin0
y= (-cos0/sin0)x + r/sin0
 
y                  -------------------------                     r
|                 /                     |    \
|     / line                            |      \
|    /                                r |   
|   /                                   |   
|  /                                    |
| /                                     |_ _ _ _  Point
|/                                      |       |
|                                       |       |
|___________________________  x         |_______|_______________________ 0 
   
         x                                      0 

Hough transform basics
-----------------------
A line in the image space can be expressed 
with two variables. 
eg 
cartesian coordinate system y= mx+c
polar coordinate system xcos0+ ysin0 =r

Hough Transformation Algorithm
--------------------------------
1. Edge detection , e.g using the canny edge detection
2. mapping of the edge points to the Hough Space and 
    storage in an accumulator.
3. Interpretation of bthe accumulatator to yield lines 
   of infinite length. The interpretation is done by thresholding
   and possibly other constraints.
4. conversion of infinite lines to finite lines.

OpenCV implements two kind of Hough Line Transforms
------------------------------------------------------

1 the Standard Hough Transform (Hough lines method)
2 the probabilistic Hough Line transform (Hough linesP  method)

'''
import cv2 
import numpy as np 

# img = cv2.imread('./data/sudoku.png')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(gray,50,150,apertureSize=3)
# lines = cv2.HoughLines(edges, 1, np.pi / 180, 200) 
# ''' 
# cv2.HoughLines(image , rho , theta,threshold)

# img = source image

# rho = distance resolution of the accumulator in pixels

# theta = angle resolution of the accumulator in radians

# threshold = Accumulator threshold parameter .Only those 
#   lines are returned that get enough votes

# lines = output vector of lines.Each line is represented
#  by a 2 or 3 element vector(p,0) or (p,0,votes). 
#  p is the distance from the coordinate origin (0,0)
#  (top left corner of the image) 0 is the rotation angle in 
#  radians.votes is the accumulator.
#  '''
# for line in lines:
#        rho , theta = line[0]
#        a = np.cos(theta)
#        b = np.sin(theta)
#        xo = a * rho
#        y0 = b * rho
#        # x1 stores the roundes off value of (r * cos(theta) - 1000 * sin(theta))
#        x1 = int(xo + 1000 * (-b))
#        # y1 stores the roundes off value of (r * sin(theta) + 1000 * cos(theta))
#        y1 = int(xo + 1000 * (a))
#        # x2 stores the roundes off value of (r * cos(theta) + 1000 * sin(theta))
#        x2 = int(xo - 1000 * (-b))
#        # y2 stores the roundes off value of (r * sin(theta) - 1000 * cos(theta))
#        y2 = int(xo - 1000 * (a))
#        cv2.line(img, (x1,y1),(x2,y2),(0,0,255),2)

# cv2.imshow('image',img)
# cv2.imshow('cannt',edges)
# k= cv2.waitKey(0)
# cv2.destroyAllWindows()


'''
The probabilistic Hough Line Transform (Hough linesP method)

HoughLines need more computation to detect the lines
but the Hough linesP is the optimisation of HoughLines
''' 

img = cv2.imread('./data/road.jpg')
img = cv2.resize(img,(600,600))
cv2.imshow('img',img)
grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(grey,50,150,apertureSize=3)
cv2.imshow('edges',edges)
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=50,maxLineGap=10)
'''
lines = cv2.HoughLinesP(image,rho,theta,threshold[,lines[,minLineLength[,maaxLineGap]])

rho = Distance resolution of the accumulator in pixels

theta = Angle resolution of the accumulator in radians
threshold = Accumulator threshold parameter. Only those lines are returned
that get enough votes(> threshold)

minLineLength = Minimum length of line .Line segment shorter than this are rejected

naxLineGap = maximum allowed gap b/w line segment to treat them as a single line
''' 
for line in lines:
       x1,y1,x2,y2 = line[0]
       ''' here lin[0] dirctly gives the x1,x2,y1,y2 points 
       to draw the line'''
       cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow('image',img)
k= cv2.waitKey(0)
cv2.destroyAllWindows()