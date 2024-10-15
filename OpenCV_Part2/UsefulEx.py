import numpy as np
import cv2

def useful_func():
    img = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

    if img is None:
        print('image load failed')
        return
    
    sum_img = np.sum(img)
    mean_img = np.mean(img, dtype=np.int32)
    print('sum:', sum_img)
    print('mean:', mean_img)

useful_func()