import numpy as np
import cv2
import time

cap = cv2.VideoCapture('./Video/Filhaal.mp4')
fps = 0
while True:
    start_time = time.time()  # Start Time
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.putText(frame, 'frame: {:.0f}'.format(fps),(30, 20),cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 255, 255), 2)
    cv2.imshow("pardeep", frame)
    if cv2.waitKey(40) == ord('q'):
        break
    time_taken = time.time() - start_time    # time taken in one second
    fps = 1 / time_taken                     # Framerate per second    # 1000/fps =
cap.release()
cv2.destroyAllWindows()