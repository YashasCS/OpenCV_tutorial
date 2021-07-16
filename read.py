import cv2 as cv
#reading images
# img = cv.imread('Photos/cat.jpg')

# cv.imshow( 'Cat',img )

# cv.waitKey(0)
#reading videos
capture = cv.VideoCapture('videos/random_video.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'): #if letter d is pressed break out of this loop
        break

capture.realease()
cv.destroyAllWindows ()
