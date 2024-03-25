import cv2
import numpy as np

# load image and convert it to HSV Color Space
image = cv2.imread('../images/one.jpg')

# Define Color Range
# define the list of boundaries
# [blue, green, red]
# any color whose 200 < r < 255 is red
# this source just kind of reiterates what I already have
# https://www.projectpro.io/recipes/detect-specific-colors-from-image-opencv

# possible color detection resource
# https://pyimagesearch.com/2016/02/15/determining-object-color-with-opencv/
boundaries = [
    ([17, 15, 100], [50, 56, 200]),
    ([86, 31, 4], [220, 88, 50]),
    ([25, 146, 190], [62, 174, 250]),
    ([103, 86, 65], [145, 133, 128])
]

# loop over the boundaries
for (lower, upper) in boundaries:
    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")
    # find the colors within the specified boundaries and apply
    # the mask
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask=mask)
    # show the images
    cv2.imshow("images", np.hstack([image, output]))
    cv2.waitKey(0)
