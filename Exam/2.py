import cv2 as cv
img = cv.imread('lenna.bmp', cv.IMREAD_GRAYSCALE)

# (1) 전체 이미지 반전
# img = cv.flip(img, 0)

# (2) 오른쪽 절반만 반전
h, w = img.shape[:2]
right_half = img[:, w//2:]
right_half_flipped = cv.flip(right_half, 1)
img[:, w//2:] = right_half_flipped

cv.imshow('result', img)
cv.waitKey()
cv.destroyAllWindows()
