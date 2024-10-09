import numpy as np
import cv2 as cv

def fun4():
    img1 = cv.imread('OpenCV_Matrix/lenna.bmp', cv.IMREAD_GRAYSCALE)

    img2 = img1[200:400, 200:400]
    img3 = img1[200:400, 200:400].copy()

    img2 += 20

    cv.imshow('img1', img1)
    cv.imshow('img2', img2)
    cv.imshow('img3', img3)
    cv.waitKey()
    cv.destroyAllWindows()

fun4()
