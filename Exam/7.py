import cv2 as cv
import numpy as np

src = cv.imread('tekapo.bmp')
                 
a = src.shape[0]
b = src.shape[1]

arr = [[2, 0, 0], [0, 2, -a]]

mat = np.array(arr).astype(np.float32)
dst = cv.warpAffine(src, mat, (0, 0))
cv.imshow('dst', dst)
cv.waitKey()