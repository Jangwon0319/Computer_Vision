import cv2
import numpy as np
from matplotlib import pyplot as plt

def calc():
    # 이미지 파일 읽기
    src1 = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)
    src2 = cv2.imread('square.bmp', cv2.IMREAD_GRAYSCALE)

    # 파일 읽기 실패 시 처리
    if src1 is None or src2 is None:
        print("Error: Image file could not be loaded. Check the file paths.")
        return

    # 두 이미지를 동일한 크기로 리사이즈 (src1의 크기로 맞춤)
    src2 = cv2.resize(src2, (src1.shape[1], src1.shape[0]))

    # 덧셈, 평균, 뺄셈, 절대 차이 연산
    dst1 = cv2.add(src1, src2)
    dst2 = cv2.addWeighted(src1, 0.5, src2, 0.5, 0.0)
    dst3 = cv2.subtract(src1, src2)
    dst4 = cv2.absdiff(src1, src2)

    # 결과 출력
    plt.subplot(231), plt.axis('off'), plt.imshow(src1, 'gray'), plt.title('src1')
    plt.subplot(232), plt.axis('off'), plt.imshow(src2, 'gray'), plt.title('src2')
    plt.subplot(233), plt.axis('off'), plt.imshow(dst1, 'gray'), plt.title('add')
    plt.subplot(234), plt.axis('off'), plt.imshow(dst2, 'gray'), plt.title('addweighted')
    plt.subplot(235), plt.axis('off'), plt.imshow(dst3, 'gray'), plt.title('subtract')
    plt.subplot(236), plt.axis('off'), plt.imshow(dst4, 'gray'), plt.title('absdiff')
    plt.show()

calc()
