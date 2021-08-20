import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat.jpg')


cv.imshow('cat', img)

# translation


def translate(x, y, img):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, dimensions, transMat)

# -x --> left
# -y --> up
# x --> right
# y --> down


translated = translate(100, 100, img)
cv.imshow('translated', translated)

cv.waitKey(0)
