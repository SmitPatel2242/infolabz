import cv2
import numpy as np

image = cv2.imread("image.jpg")
hsvimage = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
lower=np.array([0, 20, 70])
upper=np.array([50, 255, 255])
masks = cv2.inRange(hsvimage,lower,upper)
image[masks>0]=[120,138,180]
cv2.imshow("Smit",image)
cv2.waitKey(0)
cv2.destroyAllWindows()