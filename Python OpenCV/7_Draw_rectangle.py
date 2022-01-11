# Rectangle
import numpy as np
import cv2

deep = np.zeros((300,300,3),dtype="uint8")
def pardeep(imgaename,image):
    cv2.imshow(imgaename,image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#Green line
green = (0,255,0)
cv2.line(deep,(0,0),(300,300),green,3)
# pardeep("pardeeee",deep)

#Read line
red = (0,0,255)
cv2.line(deep,(300,0),(0,300),red,3)
# pardeep("pardeeee",deep)

#Green Rectangle
red1 = (0,255,0)
cv2.rectangle(deep,(10,10),(150,150),red1,1)
pardeep("pardeep",deep)

cv2.rectangle(deep,(50,200),(250,255),red,1)
pardeep("pardeep",deep)

#-1 fill color (color pixel)
cv2.rectangle(deep,(200,50),(255,200),red,-1)
pardeep("pardeep",deep)