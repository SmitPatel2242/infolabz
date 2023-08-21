import cv2
import numpy as np
image = cv2.imread("image.jpg")
rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
# blur = cv2.GaussianBlur(gray,(5,5),0)
# edges = cv2.Canny(blur,50,150)
hsvimage = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

lowercolor = np.array([0, 20, 70])
upperimage = np.array([50, 255, 255])

colormask = cv2.inRange(hsvimage,lowercolor,upperimage)
color = np.array([255,0,0])
change = np.full_like(image,color)

colored_masked_partition = cv2.bitwise_and(change,change,mask=colormask)
inverse_color_mask = cv2.bitwise_not(colormask)

non_masked_partition = cv2.bitwise_and(image,image,mask=inverse_color_mask)
# cv2.imshow('Result Image5',non_masked_partition)
result_image = cv2.add(colored_masked_partition,non_masked_partition)

cv2.imshow("Smit.jpg", result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()