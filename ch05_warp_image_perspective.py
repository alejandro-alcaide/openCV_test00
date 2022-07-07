import numpy as np

import cv2

img = cv2.imread("resources/cards.jpg")

##### will try to get one card and flatten it

# define corners (when showing the image, if you hover the cursor over the whole image, you can see such coordinates
card_points = np.float32([[111,219], [287, 188], [154, 482], [352, 440]])
# define width and height. a plain card is normally 2.5 by 3.5 inches. We will keep that aspect ratio
width, height = 250, 350
# define desired coordinates
card_coor = np.float32([[0,0], [width, 0], [0, height], [width, height]])
# transformation matrix from original points to desired points
trans_matrix = cv2.getPerspectiveTransform(card_points, card_coor)
# take original image, apply the warping with the transformed matrix, give it a size (width, height)
img_warped = cv2.warpPerspective(img, trans_matrix, (width, height))


cv2.imshow("Original", img)
cv2.imshow("Warped", img_warped)
cv2.waitKey(0)