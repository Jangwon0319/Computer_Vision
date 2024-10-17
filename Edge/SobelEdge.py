import cv2
import numpy as np

def sobel_edge():
    src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

    dx = cv2.Sobel(src, cv2.CV_32F, 1, 0)
    dy = cv2.Sobel(src, cv2.CV_32F, 0, 1)

    fmag = cv2.magnitude(dx, dy)
    mag = np.uint8(np.clip(fmag, 0, 255))
    _, edge = cv2.threshold(mag, 150, 255, cv2.THRESH_BINARY)

    cv2.imshow('src', src)
    cv2.imshow('mag', mag)
    cv2.imshow('edge', edge)
    cv2.waitKey()
    cv2.destroyAllWindows()

sobel_edge()

