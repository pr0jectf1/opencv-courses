# Import libraries
import cv2
import numpy as np
np.set_printoptions(threshold=np.inf)
import matplotlib.pyplot as plt


# Read image in GrayScale mode
image = cv2.imread("images/boy.jpg", 0)
test_roi = image[0:2,0:100]
print("Selected Region\n{}\n".format(test_roi))
image[0,0]=200

# Write the grayscale image
# cv2.imwrite("images/boyGray.jpg",image)
