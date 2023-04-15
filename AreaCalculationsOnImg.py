# cv2
import cv2
area2 = cv2.countNonZero((img1*mask)[mask])

# Numpy
import numpy as np
np.count_nonzero((img1*mask)[mask])
len(np.where((img1*mask)[mask] == 0))
np.int16([[b.pt[0], b.pt[1], b.size] for b in blobs])

# Matlab 2Numpy
#https://numpy.org/doc/stable/user/numpy-for-matlab-users.html
