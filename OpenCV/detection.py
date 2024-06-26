# use this guide for determining HSV range
# https://stackoverflow.com/questions/10948589/choosing-the-correct-upper-and-lower-hsv-boundaries-for-color-detection-withcv
import cv2
import numpy as np

# load image
img = cv2.imread("../images/one.jpg")

# Convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# dictionary to pair the color to their lower and upper hsv ranges
color_ranges = {
    'blue': [np.array([90, 100, 20]), np.array([130, 255, 255])],
    'red': [np.array([0, 150, 20]), np.array([12, 255, 255])],
    'yellow': [np.array([20, 100, 20]), np.array([30, 255, 255])],
    'orange': [np.array([10, 200, 20]), np.array([20, 255, 255])],
    'green': [np.array([35, 100, 20]), np.array([75, 255, 255])],
    'purple': [np.array([135, 100, 20]), np.array([150, 255, 255])]
    }

# iterate through each color in dictionary
for i in color_ranges:

    # define HSV color range
    lower_val = color_ranges[i][0]
    upper_val = color_ranges[i][1]

    # Threshold the HSV image - any specified color will show up as white
    mask = cv2.inRange(hsv, lower_val, upper_val)

    # check against large sum of white pixels
    # because there are small amounts of most colors on most pictures
    has_color = np.sum(mask)

    # threshold to meet to ensure large amount of color in this picture
    if has_color > 10000000:
        print(i, "color pill detected.")

# show image and apply mask to image
res = cv2.bitwise_and(img, img, mask=mask)
fin = np.hstack((img, res))

# display image with and without mask
cv2.imshow("Res", fin)
cv2.imshow("Mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

