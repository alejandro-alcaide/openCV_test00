import cv2
from alx_openCV_tools import stackImages, get_contours

img = cv2.imread("resources/shapes.png")

# convert to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# blur it
img_blur = cv2.GaussianBlur(img_gray, (7, 7), 1)
# get it's edges
img_canny = cv2.Canny(img_blur, 50, 50)

# call get_contours to get the vertices
img_contours = get_contours(img_canny)

img_stack = stackImages(.7, ([img, img_gray, img_blur], [img, img_canny, img_contours]))

cv2.imshow("shapes", img_stack)
cv2.imshow("contours only", img_contours)
cv2.waitKey(0)