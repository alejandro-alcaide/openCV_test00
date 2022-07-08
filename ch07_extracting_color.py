import cv2
import numpy as np
from alx_openCV_tools import stackImages

path_img = "resources/lambo.png"

def emptyFn(a):
    pass

# adding trackbars (a way to dynamically play with the colors' values)
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 640, 240)
# in HSV technology, the hue has 360 degrees. CV2 however has half, hence 0 to 179
# cv2.createTrackbar("Hue min", "Trackbars", 0, 179, emptyFn)
# cv2.createTrackbar("Hue max", "Trackbars", 179, 179, emptyFn)
# cv2.createTrackbar("Saturation min", "Trackbars", 0, 255, emptyFn)
# cv2.createTrackbar("Saturation max", "Trackbars", 255, 255, emptyFn)
# cv2.createTrackbar("Value min", "Trackbars", 0, 255, emptyFn)
# cv2.createTrackbar("Value max", "Trackbars", 255, 255, emptyFn)
cv2.createTrackbar("Hue min", "Trackbars", 0, 179, emptyFn)
cv2.createTrackbar("Hue max", "Trackbars", 19, 179, emptyFn)
cv2.createTrackbar("Saturation min", "Trackbars", 110, 255, emptyFn)
cv2.createTrackbar("Saturation max", "Trackbars", 240, 255, emptyFn)
cv2.createTrackbar("Value min", "Trackbars", 153, 255, emptyFn)
cv2.createTrackbar("Value max", "Trackbars", 255, 255, emptyFn)



while True:
    img = cv2.imread(path_img)

    # first we create a <hue, saturation, value> representation of our image
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue min", "Trackbars")
    h_max = cv2.getTrackbarPos("Hue max", "Trackbars")
    s_min = cv2.getTrackbarPos("Saturation min", "Trackbars")
    s_max = cv2.getTrackbarPos("Saturation max", "Trackbars")
    v_min = cv2.getTrackbarPos("Value min", "Trackbars")
    v_max = cv2.getTrackbarPos("Value max", "Trackbars")

    print("h_min:", h_min, "h_max:", h_max)
    print("s_min:", s_min, "s_max", s_max)
    print("v_min:", v_min, "v_max", v_max)


    lower_range = np.array([h_min, s_min, v_min])
    upper_range = np.array([h_max, s_max, v_max])
    # with this dynamic image, we play with the image.
    # to get our ideal values, we make everything that we don't want black and what we want we make it white
    # when done, we go back to the "Trackbars" code and adjust
    img_mask = cv2.inRange(img_hsv, lower_range, upper_range)
    # 'bitwise and' between img and img_mask (anything white in the mask will be extracted)
    img_result =  cv2.bitwise_and(img, img, mask=img_mask)

    img_stack = stackImages(.45, [img, img_hsv, img_mask, img_result])

    # cv2.imshow("mask", img_mask)
    cv2.imshow("Images", img_stack)

    cv2.waitKey(1)

