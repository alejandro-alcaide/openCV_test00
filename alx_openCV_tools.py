import cv2
import numpy as np


def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


def get_contoursA(img_canny, img_original):
    contours, hierarchy = cv2.findContours(img_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # print("area:", area)
        cv2.drawContours(img_original, cnt, -1, (255, 0, 0), 3)
    return img_original


def get_contours(img_canny):
    ih, iw = img_canny.shape
    img_blank = np.zeros((ih, iw, 3), np.uint8)
    # img_blank = np.zeros_like(img_canny)
    contours, hierarchy = cv2.findContours(img_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)

        # making sure the lines are not noise. areas must be bigger than 500 units
        if area > 500:
            # draw the contours (vertices) on the blank canvas
            cv2.drawContours(img_blank, cnt, -1, (255, 255, 255), 3)
            perimeter = cv2.arcLength(cnt, True)
            # get corner points
            corner_points = cv2.approxPolyDP(cnt, .02 * perimeter, True)
            # get each figures' corner count
            corners_count = len(corner_points)

            # this gives x0, y0, xf, yf of each figure
            x, y, w, h = cv2.boundingRect(corner_points)
            # with x, y, w, h draw boxes around each figure from point x, y to x+w, y+h
            # from these, info like coordinates, total width, height, center of the figure can be gathered
            cv2.rectangle(img_blank, (x, y), (x + w, y + h), (255, 0, 255), 3)
            figure_type = None
            if corners_count == 3:
                figure_type = "Triangle"
            elif corners_count == 4:
                aspect_ratio = float(w / h)
                print(f"4 corners aspect ratio: {aspect_ratio}")
                # we have a pct of error
                if aspect_ratio > 0.98 and aspect_ratio < 1.03:
                    figure_type = "Square"
                else:
                    figure_type = "Rectangle"
            elif corners_count == 8:
                figure_type = "Circle"

            # write in the center of our figure
            cv2.putText(
                img_blank,
                figure_type,
                (x + (w // 2) - 10, y + (h // 2) - 10),
                cv2.FONT_HERSHEY_COMPLEX,
                .35,
                (255, 0, 255),
                1
            )

            print(f"area: {area}, perimeter: {perimeter}, corners_count: {corners_count}, x:{x}, y:{y}, w: {w}, h:{h},"
                  + f" figure_type: {figure_type}")
    return img_blank
