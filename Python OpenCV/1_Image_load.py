import numpy as np
import cv2

img = cv2.imread('images/bird.jpg')
print(img)
print(img.shape)

cv2.imshow('pardeep',img)
#cv2.waitKey(2000)          # image show for a second as per you entered "Waitkey"
cv2.waitKey(0)              # image automatic close when you press any key
cv2.destroyAllWindows()