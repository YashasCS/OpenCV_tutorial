import cv2 as cv
import mediapipe as mp
import time

cap =  cv.VideoCapture(0)  # to run a webcam

mpHands = mp.solutions.hands        # a formality to use this model later in other projects
hands = mpHands.Hands()         # this class uses only rgb images so convert also default params
mpDraw = mp.solutions.drawing_utils    # mediapipe library

pTime = 0
cTime = 0
while(cap.isOpened()):
    success, img = cap.read()

    if(success!=True):
        break

    # cv.imshow("image",img)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)     # method inside obj hands called process to process the frames
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:    # counts the no of hands and landmarks them
            for id, lm in enumerate (handLms.landmark):
                # print(id,lm)
                h, w, c = img.shape
                cx,cy = int(lm.x*w), int(lm.y*h)
                print(id,cx,cy)
                if id == 4:
                    cv.circle(img, (cx,cy), 30, (255,255,0),cv.FILLED)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)  # handlms is the single hand

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv.putText(img, str(int(fps)),(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)

    cv.imshow("image",img)     # precedence is very important
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()

