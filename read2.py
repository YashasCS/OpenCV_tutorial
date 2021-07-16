import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    # WORK ON IMAGES, VIDEOS AND LOVE VIDEOS
    width = int (frame.shape[1]*scale)
    height = int (frame.shape[0]*scale)

    dimensions = (width,height)

    return cv.resize (frame,dimensions,interpolation=cv.INTER_AREA)

def changeRes(width, height):
    #WORKS ONLY ON LIVE VIDEOS
    capture.set(3,width)
    capture.set(4.height)

#READING videos
capture = cv.VideoCapture('videos/random_video.mp4')

while True :
    isTrue, frame=capture.read()
    cv.imshow('video',frame)

    frame_Resized = rescaleFrame(frame)
    cv.imshow('video resized ',frame_Resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
