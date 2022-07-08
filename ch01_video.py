import cv2

# from a file
#cap = cv2.VideoCapture("resources/v00.mp4")
# from a video device. 0 means the first video device available
cap = cv2.VideoCapture(0)
# width
cap.set(3,640)
# height
cap.set(4,480)
# brightness
cap.set(10, 90)

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    # ord('q') means that you need to press 'q' to quit
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break