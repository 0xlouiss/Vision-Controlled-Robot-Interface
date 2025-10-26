import cv2
import os
import mediapipe as mp

# self.handsMp - mp.solutions.hands # the hand recognition algorithm
# self.hands = self.handsMp.Hands() # detect the hand
# self.mpDraw= mp.solutions.drawing_utils # draws the detect keys


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

if not cap.isOpened():
    print("Camera not opening")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow('Camera Test', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
