import cv2


def emptyFn(a):
    pass

# adding trackbars (a way to dynamically play with the colors' values)
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 640, 240)
# in HSV technology, the hue has 360 degrees. CV2 however has half, hence 0 to 179
cv2.createTrackbar("Hue min", "Trackbars", 0, 179, emptyFn)
cv2.createTrackbar("Hue max", "Trackbars", 179, 179, emptyFn)
cv2.createTrackbar("Saturation min", "Trackbars", 0, 255, emptyFn)
cv2.createTrackbar("Saturation max", "Trackbars", 255, 255, emptyFn)
cv2.createTrackbar("Value min", "Trackbars", 0, 255, emptyFn)
cv2.createTrackbar("Value max", "Trackbars", 255, 255, emptyFn)



while True:
    img = cv2.imread("resources/lambo.png")

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

    cv2.imshow("Output", img)
    cv2.imshow("hsv", img_hsv)
    cv2.waitKey(0)

