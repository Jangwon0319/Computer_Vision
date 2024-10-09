import cv2 as cv

img = cv.imread('OpenCV_Matrix/lenna.bmp')

if img is None:
    print('Image load failed')
    exit()

cv.imshow('image', img)
cv.waitKey()