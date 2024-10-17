import cv2
import numpy as np

def canny_edge():
    src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

    dst1 = cv2.Canny(src, 50, 100)
    dst2 = cv2.Canny(src, 50, 150)

    cv2.imshow('src', src)
    cv2.imshow('dst1', dst1)
    cv2.imshow('dst2', dst2)

    cv2.waitKey()
    cv2.destroyAllWindows()

canny_edge()

