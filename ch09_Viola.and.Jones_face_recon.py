import cv2


# face cascade is a precompiled generic face detection xml
face_cascade = cv2.CascadeClassifier("resources/haarcascades/haarcascade_frontalface_default.xml")

path_to_img = "resources/lena.png"
img = cv2.imread(path_to_img)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(img_gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)



cv2.imshow("Output", img)
cv2.waitKey(0)