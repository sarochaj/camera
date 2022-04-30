import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
while True:
    ret, frame = cap.read()
    cv.imshow('test',frame)
    if cv.waitKey(1) == ord('='):
        break

cap.release()
cv.destroyAllWindow()