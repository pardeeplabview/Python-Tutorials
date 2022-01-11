import numpy as np
import cv2

img = cv2.imread('images/bird.jpg')
def deep(imagename,image):
    cv2.imshow(imagename,image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# deep('pardeep',img)

## access 200 row and 200columns
# corner = img[0:200,0:200]
# deep('corner_image',corner)

# access 100 row and 100columns and darg green color
green = (0,0,128)
img[0:200,0:200] = green
deep('image_name',img)
