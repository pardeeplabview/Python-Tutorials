import numpy as np
import cv2

deep = np.zeros((300,300,3),dtype='uint8')
def pardeep(imagename,image):
    cv2.imshow(imagename,image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#Green line
green = (0,255,0)
cv2.line(deep,(0,0),(300,300),green,3)
pardeep("pardeeee",deep)

#Read line
red = (0,0,255)
cv2.line(deep,(300,0),(0,300),red,3)
pardeep("pardeeee",deep)
