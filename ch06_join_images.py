import cv2
import numpy as np

img = cv2.imread("resources/lena.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_cards = cv2.imread("resources/cards.jpg")
img_lambo = cv2.imread("resources/lambo.png")

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


horizontally_stacked_images = np.hstack((img, img))
vertically_stacked_images = np.vstack((img, img))
fn_img_stack = stackImages(.5,[img,img,img])
fn_img_2stack = stackImages(.4,([img,img_gray,img], [vertically_stacked_images,horizontally_stacked_images,img_gray], [img_lambo, img_cards, img_gray]))

cv2.imshow("Horizontally stacked images", horizontally_stacked_images)
cv2.imshow("Vertically stacked images", vertically_stacked_images)
cv2.imshow("Function stacked images", fn_img_stack)
cv2.imshow("Function stacked images with several lines", fn_img_2stack)
cv2.waitKey(0)