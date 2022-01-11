import numpy as np
import cv2

deep = np.zeros((400,400,3),dtype="uint8")
def pardeep(imagename,image):
    cv2.imshow(imagename,image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
pardeep("draw",deep)
