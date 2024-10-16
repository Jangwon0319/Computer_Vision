import numpy as np
import cv2

def affine_shear():
    src = cv2.imread('tekapo.bmp')

    rows = src.shape[0]
    cols = src.shape[1]

    mx = 0.3
    affine_mat = np.array([[1, mx, 0],
                           [0, 1, 0]]).astype(np.float32)
    
    dst = cv2.warpAffine(src, affine_mat, (int(cols + rows * mx), rows))

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

affine_shear()
