import numpy as np
import cv2

def blurring_mean():
    src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

    cv2.imshow('src', src)

    for ksize in range(3, 9, 2):
        dst = cv2.blur(src, (ksize, ksize))

        desc = "Mean: %dx%d" %(ksize, ksize)
        cv2.putText(dst, desc, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, 255, 1, cv2.LINE_AA)

        cv2.imshow('dst', dst)
        cv2.waitKey()
    
    cv2.destroyAllWindows()

blurring_mean()