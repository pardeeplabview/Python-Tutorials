import numpy as np
import cv2

img = cv2.imread('images/pardeep.png')
img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)

cv2.imshow('brg',img)
cv2.imshow('rgb',img_rgb)
cv2.imshow('gray',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()