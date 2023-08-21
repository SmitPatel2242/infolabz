import cv2
import numpy as np

# Load the image
image = cv2.imread('img_1.png')

# Convert the image to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the lower and upper bounds for blue color in HSV format
blue_lower = np.array([90, 50, 50])
blue_upper = np.array([130, 255, 255])

# Create a mask for blue pixels
blue_mask = cv2.inRange(hsv_image, blue_lower, blue_upper)

# Change blue pixels to red in the original BGR image
image[blue_mask > 0] = [0, 0, 255]  # Change blue to red (BGR value)

# Save or display the modified image
cv2.imwrite('output_image.jpg', image)
cv2.imshow('Modified Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
