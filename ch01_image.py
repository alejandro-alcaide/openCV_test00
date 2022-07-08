import cv2

path_to_img = "resources/lena.png"
img = cv2.imread(path_to_img)





cv2.imshow("Output", img)
cv2.waitKey(0)