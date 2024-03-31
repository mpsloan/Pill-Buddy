# use this guide for determining HSV range
# https://stackoverflow.com/questions/10948589/choosing-the-correct-upper-and-lower-hsv-boundaries-for-color-detection-withcv
import cv2
import numpy as np
# load image
img = cv2.imread("../images/two.jpg")
# Convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# BLUE
# define range wanted color in HSV
lower_val = np.array([90,100,20])
upper_val = np.array([130,255,255])

# Threshold the HSV image - any green color will show up as white
mask = cv2.inRange(hsv, lower_val, upper_val)

# if there are any white pixels on mask, sum will be > 0
hasBlue = np.sum(mask)
if hasBlue > 10000000:
    print('Blue detected!')
else:
    print('No blue')

# YELLOW
lower_val = np.array([20,100,20])
upper_val = np.array([30,255,255])

mask = cv2.inRange(hsv, lower_val, upper_val)

hasYellow = np.sum(mask)
if hasYellow > 10000000:
    print('Yellow detected!')
else:
    print('No yellow')

# RED
lower_val = np.array([0,150,20])
upper_val = np.array([12,255,255])

mask = cv2.inRange(hsv, lower_val, upper_val)

hasRed = np.sum(mask)
if hasRed > 10000000:
    print('Red detected!')
else:
    print('No red')

# show image
# apply mask to image
res = cv2.bitwise_and(img,img,mask=mask)
fin = np.hstack((img,res))
# display image
cv2.imshow("Res", fin)
cv2.imshow("Mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
