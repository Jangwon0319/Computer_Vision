import numpy as np
import cv2 as cv

def func1():
    img1 = cv.imread('OpenCV_Matrix/cat.bmp', cv.IMREAD_GRAYSCALE)

    if img1 is None:
        print('Image load fail')
        return
    
    print('type(img1): ', type(img1))
    print('img1.shape: ', img1.shape)
    
    if len(img1.shape) == 2:
        print('img1 is a grayscale image')
    elif len(img1.shape) == 3:
        print('img1 is a truecolor image')
    
    cv.imshow('img1', img1)
    cv.waitKey()
    cv.destroyAllWindows()

func1()
