import cv2
import numpy
import numpy as np

img = cv2.imread("resources/lena.png")

# change color
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# blur using gauss process (source img, grain size pair, sigmaX (not sure)
img_blurred = cv2.GaussianBlur(img, (7, 7), 0)

# edge detector
img_edges = cv2.Canny(img, 100, 100)

# dilation
# we will need to do matrix operations. we create an eight bit 5x5 kernel with ones (1) in it
kernel = np.ones((2, 2), np.uint8) # changed to 2x2
# we dilate our edged image against the kernel a set number of times
img_dilated = cv2.dilate(img_edges,kernel, iterations=1)

# erode
img_eroded = cv2.erode(img_dilated, kernel, iterations=1)

cv2.imshow("BGR to Gray image", img_gray)
cv2.imshow("Blurred image", img_blurred)
cv2.imshow("Edge image", img_edges)
cv2.imshow("Dilated edges image", img_dilated)
cv2.imshow("Eroded<-dilated<-edges<-image", img_eroded)
cv2.waitKey(0)
