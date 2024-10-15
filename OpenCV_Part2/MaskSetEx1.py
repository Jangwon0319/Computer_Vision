import cv2
import numpy as np

def mask_setTo():
    src = cv2.imread('lenna.bmp', cv2.IMREAD_COLOR)
    mask = cv2.imread('mask_smile.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None or mask is None:
        print('image load fail')
        return
    
    src[mask > 0] = (0, 255, 255)

    cv2.imshow('src', src)
    cv2.imshow('mask', mask)
    cv2.waitKey()
    cv2.destroyAllWindows()

mask_setTo()