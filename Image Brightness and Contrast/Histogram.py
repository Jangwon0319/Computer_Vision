import numpy as np
import cv2

def calcGrayHist(img):
    channels = [0]
    histSize = [256]
    histRange = [0, 256]

    hist = cv2.calcHist([img], channels, None, histSize, histRange)

    return hist

def getGrayHistImage(hist):
    _, histMax, _, _ = cv2.minMaxLoc(hist)

    imgHist = np.ones((100, 256), np.uint8) * 255
    for x in range(imgHist.shape[1]):
        pt1 = (x, 100)
        pt2 = (x, 100 - int(hist[x, 0] * 100 / histMax))
        cv2.line(imgHist, pt1, pt2, 0)

    return imgHist

src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)
hist = calcGrayHist(src)
hist_img = getGrayHistImage(hist)

cv2.imshow('src', src)
cv2.imshow('srcHist', hist_img)
cv2.waitKey()
cv2.destroyAllWindows()