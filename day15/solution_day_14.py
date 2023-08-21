import cv2
import numpy as np

image = cv2.imread("img_1.png")
resize = cv2.resize(image, (700,700))
hsv_image = cv2.cvtColor(resize, cv2.COLOR_BGR2HSV)

lower_color=np.array([100,50,50])
upper_color=np.array([130,255,255])

color_mask = cv2.inRange(hsv_image, lower_color, upper_color)

color = np.array([0,120,255])
red_color = np.full_like(resize,color)

colored_masked_partition = cv2.bitwise_and(red_color,red_color,mask=color_mask)

inverse_color_mask = cv2.bitwise_not(color_mask)

non_masked_partition = cv2.bitwise_and(resize,resize,mask=inverse_color_mask)
# cv2.imshow('Result Image5',non_masked_partition)
result_image = cv2.add(colored_masked_partition,non_masked_partition)

cv2.imshow('Result Image',result_image)
cv2.imshow('Result Image1',color_mask)
cv2.imshow('Result Image2',colored_masked_partition)
cv2.imshow('Result Image3',inverse_color_mask)


cv2.waitKey(0)
cv2.destroyAllWindows()