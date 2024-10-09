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

def func2():
    img1 = np.empty((480, 640), np.uint8)
    img2 = np.zeros((480, 640, 3), np.unit8)
    img3 = np.ones((480, 640), np.int32)
    img4 = np.full((480, 640), 0, np.float32)

    mat1 = np.array([[11, 12, 13, 14],
                     [21, 22, 23, 24],
                     [31, 32, 33, 34]]).astype(np.unit8)
    
    mat1[0, 1] = 100
    mat1[2, :] = 200

    print(mat1)

func2()