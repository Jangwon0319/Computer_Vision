import cv2 as cv
img = cv.imread('lenna.bmp', cv.IMREAD_GRAYSCALE)

# (1) 전체 이미지 색깔 반전
img = cv.bitwise_not(img)

# (2) 오른쪽 절반만 색깔 반전
# h, w = img.shape[:2]
# right_half = img[:, w//2:]
# right_half_inverted = cv.bitwise_not(right_half)
# img[:, w//2:] = right_half_inverted

cv.imshow('result', img)
cv.waitKey()
cv.destroyAllWindows()
