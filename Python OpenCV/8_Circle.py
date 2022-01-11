import time

import numpy as np
import cv2

deep = np.zeros((800,800,3),dtype = "uint8")
def pardeep(imagename,image):
    cv2.imshow(imagename,image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

centerX,centerY = (deep.shape[1]//2 , deep.shape[0] //2)
print("Window center X= ",centerX,"\n")
print("Window center Y= ",centerY,"\n")

#one circle radiour is 150
# Color_white = (255,255,255)
# cv2.circle(deep,(centerX,centerX),150,Color_white)
# pardeep("dede",deep)

#one circle radiour is 100
# Color_white = (255,255,255)
# cv2.circle(deep,(centerX,centerX),100,Color_white)
# pardeep("dede",deep)

#Multiple circles
Color_white = (255,255,255)
for r in range(0,400,10):
    cv2.circle(deep,(centerX,centerY),r,Color_white)
pardeep("circle",deep)

#Example
# color_whie = (255,255,255)
# r = 0
# while r<400:
#     cv2.circle(deep, (centerX, centerY), r, color_whie)
#     r = r+10
#     pardeep("circle", deep)

