import cv2
print('cv2 package imported successfuly')

img = cv2.imread("resources/lambo.png")
print('img.shape=', img.shape)

# resizing
img_resized = cv2.resize(img, (300, 200))

# crop (height, width)
img_cropped = img[0:200, 200:500]


cv2.imshow("Image", img)
cv2.imshow("Resized image", img_resized)
cv2.imshow("Cropped image", img_cropped)
cv2.waitKey(0)