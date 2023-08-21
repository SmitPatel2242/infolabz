import cv2
import numpy as np

image = cv2.imread("img_1.png")
resize = cv2.resize(image,(500,500))
hsvimage = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

lowercolor = np.array([90,50,50])
upperimage = np.array([130,255,255])

colormask = cv2.inRange(hsvimage, lowercolor,upperimage)
image[colormask > 0]=[0, 0, 255]
cv2.imshow("ImageD",image)
cv2.waitKey(0)
cv2.destroyAllWindows()