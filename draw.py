import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3),dtype='uint8')    #uint8 is basically the datatype of an image
#img = cv.imread('Photos/cat.jpg')
cv.imshow('Blank',blank)
#cv.imshow('cat',img)

# 1. painting an image a certain colour
# blank[200:300,390:400] = 0,0,255
# cv.imshow('red',blank)

# 2. draw a rectangle
# cv.rectangle(blank,(0,0),(200,200),(0,200,0), thickness= -1 )   #or even cv.FILLED
# cv.imshow('rectangle',blank)
#
# # 3. draw a circle
# cv.circle(blank,(250,250),40,(0,255,0),thickness=cv.FILLED)
# cv.imshow('circle',blank)
#
# # 4. draw a line
# cv.line(blank, (0,0),(250,250),(255,255,255),thickness=3)
# cv.imshow('line',blank)

# 5. text on an image
cv.putText(blank,'Hello World',(200,200),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,0),2)
cv.imshow ('text',blank)

cv.waitKey(0)
