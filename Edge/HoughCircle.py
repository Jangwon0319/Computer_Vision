import cv2
import numpy as np

def hough_circles():
    src = cv2.imread('coins.png', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('image load fail')
        return
    
    blurred = cv2.blur(src, (3, 3))
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, 50,
                               param1=150, param2=30)
    
    dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

    if circles is not None:
        for i in range(circles.shape[1]):
            cx, cy, radius = circles[0][i]
            cx, cy, radius = int(cx), int(cy), int(radius)  # 정수형으로 변환
            cv2.circle(dst, (cx, cy), radius, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

hough_circles()
