import cv2
import numpy as np

def on_mouse(event, x, y, flags, param):
    global cnt, src_pts

    if event == cv2.EVENT_LBUTTONDOWN:
        if cnt < 4:
            src_pts[cnt, :] = np.array([x, y]).astype(np.float32)
            cnt += 1

            cv2.circle(src, (x, y), 5, (0, 0, 255), -1)
            cv2.imshow('src', src)

        if cnt == 4:
            w = 200
            h = 300

            dst_pts = np.array([[0, 0],
                                [w - 1, 0],
                                [w - 1, h - 1],
                                [0, h - 1]]).astype(np.float32)
            
            pers_mat = cv2.getPerspectiveTransform(src_pts, dst_pts)

            dst = cv2.warpPerspective(src, pers_mat, (w, h))

            cv2.imshow('dst', dst)

cnt = 0
src_pts = np.zeros([4, 2], dtype=np.float32)  # 네 개의 좌표 저장을 위한 배열 생성

src = cv2.imread('card.bmp')  # 입력 이미지 로드

if src is None:
    print('Image load failed!')
    exit()

cv2.namedWindow('src')  # 창 생성
cv2.setMouseCallback('src', on_mouse)  # 마우스 이벤트 콜백 설정

cv2.imshow('src', src)  # 원본 이미지 출력
cv2.waitKey(0)  # 키 입력 대기
cv2.destroyAllWindows()  # 모든 창 닫기