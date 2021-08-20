import cv2 as cv
import mediapipe as mp
import time

class handDetector ():
    def __init__(self, mode = False, maxHands = 2, detectionCon=0.5, trackingCon=0.5):
        self.mode= mode
        self.maxHands=maxHands
        self.detectionCon=detectionCon
        self.trackingCon=trackingCon

        self.mpHands = mp.solutions.hands  # a formality to use this model later in other projects
        self.hands = self.mpHands.Hands( self.mode , self.maxHands, self.detectionCon, self.trackingCon)  # this class uses only rgb images so convert also default params
        self.mpDraw = mp.solutions.drawing_utils  # mediapipe library

    def findHands(self,img, draw=True):
        # cv.imshow("image",img)
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        # self.results.multi_hand_landmarks = []
        self.results = self.hands.process(imgRGB)  # method inside obj hands called process to process the frames
        # print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:  # counts the no of hands and landmarks them
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)  # handlms is the single hand
        return img

    def findPosition(self,img, handNo = 0, draw=True):      # for a particular hand only
        # self.results.multi_hand_landmarks = []
        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                # print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)
                lmList.append([id, cx, cy])
                if id==6:
                    cv.circle(img, (cx,cy),5, (255,255,0),cv.FILLED )


        return lmList

def main ():
    pTime = 0
    cTime = 0
    cap = cv.VideoCapture(0)  # to run a webcam
    detector = handDetector()

    while cap.isOpened():
        # capture frame by frame
        success, img = cap.read()
        # img = detector.findHands(img)

        if (success != True):
            break

        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        if len(lmList)!=0:
            print (lmList[4])

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        cv.imshow("image",img)     # precedence is very important

        if cv.waitKey(1) & 0xFF == ord('q'):
            break


if (__name__ == "__main__"):
    main()
cv.destroyAllWindows()
