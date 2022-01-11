import numpy as np
import cv2

deep = np.zeros((800,800,3),dtype = "uint8")
def pardeep(imagename,image):
    cv2.imshow(imagename,image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

for r in range(0,25):
    radous = np.random.randint(5,100)
    color = np.random.randint(0,255,size=(3,)).tolist()
    pt = np.random.randint(0,800,size=(2,))
    cv2.circle(deep,tuple(pt),radous,color,-1)
pardeep("pardeep",deep)

#Save Image
print(cv2.imwrite('images/Color_Random.png',deep))


#Example
# while(1):
#     for r in range(0,25):
#         radous = np.random.randint(5,100)
#         color = np.random.randint(0,255,size=(3,)).tolist()
#         pt = np.random.randint(0,800,size=(2,))
#     cv2.circle(deep,tuple(pt),radous,color,-1)
#     pardeep("pardeep",deep)