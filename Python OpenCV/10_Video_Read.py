import numpy as np
import cv2

cap = cv2.VideoCapture('./Video/Filhaal.mp4')
while True:
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imshow("pardeep",frame)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()