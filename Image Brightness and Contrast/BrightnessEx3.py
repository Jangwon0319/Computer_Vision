import numpy as np
import cv2

def saturated(value):
    if value > 255:
        value = 255
    elif value < 0:
        value = 0

    return value

def brigntness3():
    src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print("Image load fail")
        return
    
    # 연산 전 int32 타입으로 변환하여 오버플로우 방지
    dst = np.empty(src.shape, dtype=np.int32)
    
    # 각 픽셀 값에 100을 더하고 포화 처리 수행
    for y in range(src.shape[0]):
        for x in range(src.shape[1]):
            dst[y, x] = saturated(int(src[y, x]) + 100)  # 정수형으로 변환 후 덧셈 연산

    # 최종적으로 다시 uint8로 변환하여 이미지 저장
    dst = np.uint8(dst)

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

brigntness3()