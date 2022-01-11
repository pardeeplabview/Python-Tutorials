import numpy as np
import cv2

img = cv2.imread('images/bird.jpg')
print("image matrix\n",img)
print("image matrix shape\n",img.shape)
b,g,r = cv2.split(img)
print("image split blue\n",b)

cv2.imshow('deep_color',img)
cv2.imshow('blue_color',b)
cv2.imshow('green_color',g)
cv2.imshow('red_color',r)
cv2.waitKey(0)
cv2.destroyAllWindows()
