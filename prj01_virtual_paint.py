import cv2
import numpy as np

##
## using ch01 video feed and ch07 extracting color
##


# video camera values
frame_width = 640
frame_height = 480
cap = cv2.VideoCapture(0)
cap.set(3, frame_width)
cap.set(4, frame_height)
cap.set(10, 150)

hsv_colors = [
    [5, 107, 0, 19, 255, 255, "orange"],  # orange
    [133, 56, 0, 159, 156, 255, "purple"],  # purple
    [57, 76, 0, 100, 255, 255, "green"],  # green
    [90, 48, 0, 118, 255, 255, "blue"]  # blue
]

# blue, green, red
bgr_colors = [
    [51, 153, 255],
    [255, 0, 255],
    [0, 255, 0],
    [255, 0, 0]
]

my_points = []  ## [x , y , colorId ]


def findColor(analyzed_img, hsv_colors_lit, bgr_colors_list):
    img_hsv = cv2.cvtColor(analyzed_img, cv2.COLOR_BGR2HSV)
    count = 0
    new_points = []
    for color_item in hsv_colors_lit:
        lower_range = np.array(color_item[0:3])
        upper_range = np.array(color_item[3:6])
        img_mask = cv2.inRange(img_hsv, lower_range, upper_range)

        cx, cy = get_obj_contours(img_mask)

        cv2.circle(img_result, (cx, cy), 15, bgr_colors_list[count], cv2.FILLED)
        if cx != 0 and cy != 0:
            new_points.append([cx, cy, count])
        count += 1

    return new_points


def get_obj_contours(img_mask):
    contours, hierarchy = cv2.findContours(img_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            # cv2.drawContours(img_result, cnt, -1, (255, 255, 255), 3)
            peri = cv2.arcLength(cnt, True)
            corners_count = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(corners_count)
    return x + w // 2, y


def draw_on_canvas(points_list, bgr_colors_list):
    for cpt in points_list:
        cv2.circle(img_result, (cpt[0], cpt[1]), 10, bgr_colors_list[cpt[2]], cv2.FILLED)


while True:
    success, img = cap.read()
    img_result = img.copy()
    new_points = findColor(img, hsv_colors, bgr_colors)

    if len(new_points) != 0:
        for pt in new_points:
            my_points.append(pt)
    if len(my_points) != 0:
        draw_on_canvas(my_points, bgr_colors)

    # cv2.imshow("Video", img)
    cv2.imshow("Final Img", img_result)
    # ord('q') means that you need to press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
