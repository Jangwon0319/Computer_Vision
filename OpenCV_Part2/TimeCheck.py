import numpy as np
import cv2

def time_inverse():
    src = cv2.imread('OpenCV_Part2/lenna.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed')
        return

    dst = np.empty(src.shape, dtype=src.dtype)

    tm = cv2.TickMeter()
    tm.start()

    for y in range(src.shape[0]):
        for x in range(src.shape[1]):
            dst[y, x] = 255 - src[y,x]

    tm.stop()
    print('Image inverse implementation took %4.3f ms.' % tm.getTimeMilli())

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

time_inverse()

