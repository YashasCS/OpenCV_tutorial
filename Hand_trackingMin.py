import cv2 as cv
import mediapipe as mp
import time

cap =  cv.VideoCapture(0)  # to run a webcam

while(cap.isOpened()):
    success, img = cap.read()

    if(success!=True):
        break

    cv.imshow("image",img)

    cv.waitKey(1)

