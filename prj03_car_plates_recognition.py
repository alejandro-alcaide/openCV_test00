import cv2

#############################################
frame_width = 640
frame_height = 480
car_plate_cascade = cv2.CascadeClassifier("resources/haarcascades/haarcascade_russian_plate_number.xml")
min_area = 200
color = (255, 0, 255)
###############################################
# video file (russian plate is no. 34)
# cap = cv2.VideoCapture("resources/car_plates/EU_2021_[360p@1fps].mp4")
# feed
cap = cv2.VideoCapture(0)
cap.set(3, frame_width)
cap.set(4, frame_height)
cap.set(10, 150)
count = 0

while True:
    success, img = cap.read()
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    car_plates = car_plate_cascade.detectMultiScale(img_gray, 1.1, 10)
    for (x, y, w, h) in car_plates:
        area = w * h
        if area > min_area:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
            cv2.putText(img, "Car Plate", (x, y - 5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
            # roi = region of interest
            img_roi = img[y:y + h, x:x + w]
            cv2.imshow("Image ROI", img_roi)

    cv2.imshow("Result", img)

    # use this one if scanning the video peek by peek (not pic)
    # cv2.waitKey(0)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("resources/car_plate_scans/car_plate_" + str(count) + ".jpg", img_roi)
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Scan saved", (150, 265), cv2.FONT_HERSHEY_DUPLEX,
                    2, (0, 0, 255), 2)
        cv2.imshow("Result", img)
        cv2.waitKey(500)
        count += 1
