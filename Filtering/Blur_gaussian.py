import numpy as np
import cv2

def blurring_gaussian():
    src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('image load fail')
        return
    
    cv2.imshow('src', src)

    for sigma in range(1, 6):
        dst = cv2.GaussianBlur(src, (0,0), sigma)

        desc = "Gaussian : sigma = %d" % (sigma)
        cv2.putText(dst, desc, (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, 255, 1, cv2.LINE_AA)

        cv2.imshow('dst', dst)
        cv2.waitKey()

    cv2.destroyAllWindows()

blurring_gaussian()