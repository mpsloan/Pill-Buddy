import cv2
import numpy as np

# load image and convert it to HSV Color Space
img = cv2.imread('../images/one.jpg')
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define Color Range
lower_range = (0, 50, 50)
upper_range = (10, 255, 255)
mask = cv2.inRange(hsv_img, lower_range, upper_range)

# Apply mask to image
color_image = cv2.bitwise_and(img, img, mask=mask)

# Display color image
cv2.imshow('Color Image', color_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
