import cv2
print('cv2 package imported successfuly')

img = cv2.imread("resources/lena.png")
cv2.imshow("Output", img)
cv2.waitKey(0)