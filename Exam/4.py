import cv2 as cv

a = cv.imread('lenna.bmp', cv.IMREAD_COLOR)      # 색상 이미지
b = cv.imread('mask_smile.bmp', cv.IMREAD_GRAYSCALE)  # 마스크 이미지 (흑백)
c = cv.imread('rose.bmp', cv.IMREAD_COLOR)       # 배경 이미지

# 마스크 크기를 a와 맞춤
b_resized = cv.resize(b, (a.shape[1], a.shape[0]))

# 마스크를 3채널로 변환 (컬러 이미지에 적용할 수 있도록)
b_resized_3ch = cv.merge([b_resized, b_resized, b_resized])

# a의 내용을 b_resized 마스크를 사용해 r에 복사
r = cv.bitwise_or(cv.bitwise_and(a, b_resized_3ch), cv.bitwise_and(c, cv.bitwise_not(b_resized_3ch)))

# 결과 출력
cv.imshow('result', r)
cv.waitKey()
cv.destroyAllWindows()
