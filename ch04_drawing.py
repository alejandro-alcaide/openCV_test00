import cv2
import numpy as np

# plain 512x512x3 image with 8 bits per pixel. all zeroes gives a black square
img = np.zeros((512, 512, 3), np.uint8)

# coloring all pink img[:] means that for all values in the whole matrix, we will set the new values
img[:] = 255, 0, 255

# creating a line (this goes horizontal first, vertical second) from 0,0 to 150,450, color blue, thickness 3
cv2.line(img,(0,0), (150, 450), (255, 0, 0), 3)

# green filled rectangle (cv2.FILLED instead of thickness)
cv2.rectangle(img, (200,0), (500, 150), (0, 0, 255), cv2.FILLED)

# circle
cv2.circle(img, (250, 250), 50, (0,0,0), 3)

# text
cv2.putText(img, "openCV test 00 ch03", (150, 350), cv2.FONT_HERSHEY_COMPLEX, 0.75, (0,0,0), 1)


cv2.imshow("Image", img)
cv2.waitKey(0)