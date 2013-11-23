import cv2
import time

cam = cv2.VideoCapture(0)
cv2.namedWindow("Test", cv2.CV_WINDOW_AUTOSIZE)

while True:
    cv2.imshow("Test", cam.read()[1])

    # for n in range(0, 10):
    # time.sleep(0.2)
        
    key = cv2.waitKey(10)
    if key == 27:
        break

