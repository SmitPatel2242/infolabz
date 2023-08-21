import cv2
import numpy as np

# Load the image
image = cv2.imread('7.jpg')
resize =  cv2.resize(image,(500,300))
# Iterate through each pixel and change blue to red


print(resize.shape)

# Save or display the modified image
cv2.imwrite('output_image.jpg', resize)
cv2.imshow('Modified Image', resize)
cv2.waitKey(0)
cv2.destroyAllWindows()