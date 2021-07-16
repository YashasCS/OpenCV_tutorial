import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('cat',img )

# converting to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2HSV_FULL)      #cvt stands for converting colour
cv.imshow('gray',gray)

# blurring an image
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)   # always has to be odd the kernel size
cv.imshow('blur',blur)

# edge cascade
canny = cv.Canny(img, 150, 175)
cv.imshow ('Canny Edge',canny)

#dilate image
dilate = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('dilated',dilate)

cv.waitKey(0)
