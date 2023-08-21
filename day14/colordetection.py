import cv2
import numpy as np

image = cv2.imread("img_1.png")
# image = cv2.imread("C:/Users/smitp/Desktop/Infolabz/day14/img_1.png")
resize = cv2.resize(image,(500,500))
hsvimage = cv2.cvtColor(resize,cv2.COLOR_RGB2HSV)

lowercolor = np.array([0,50,50])
upperimage = np.array(([255,255,255]))
# lowercolor = np.array([110, 100, 100])
# upperimage = np.array(([130,255,255]))
# lowercolor = np.array([150, 140, 60])
# upperimage = np.array(([255, 255, 180]))
colormask = cv2.inRange(hsvimage, lowercolor,upperimage)
detectedimage = cv2.bitwise_and(resize,resize,mask=colormask)
cv2.imshow("Image",resize)
cv2.imshow("ImageD",detectedimage)
cv2.imshow("ImageH",hsvimage)
cv2.waitKey(0)
cv2.destroyAllWindows()