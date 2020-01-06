# a.0.1
# code by EslerKang

import cv2
# import numpy as np
import pyzbar.pyzbar as pyzbar
import time

CAM_NUM = 0

cap = cv2.VideoCapture(CAM_NUM)

font = cv2.FONT_HERSHEY_PLAIN

# fps 표시를 위해 이전 시간 저
prev_time = 0

# 너비
cap.set(3, 640)

# 높이
cap.set(4, 480)

if cap.isOpened():
    detector = cv2.QRCodeDetector()
    while True:
        _, frame = cap.read()

        # 흑백영상으로 바꿈
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # fps 계산, 출력
        cur_time = time.time()
        past_time = cur_time - prev_time
        prev_time = cur_time
        fps = 1/past_time
        fps_str = "FPS : %.1f" % fps
        cv2.putText(frame, fps_str, (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))

        decodedObjects = pyzbar.decode(frame)
        for obj in decodedObjects:

            # QR 코드값 화면에 출력
            cv2.putText(frame, (str(obj.data).split('_'))[len(str(obj.data).split('_'))-1], (50, 50), font, 2,
                        (255, 0, 0), 3)

            # QR 코드값 검사 후 표시(추후 서버로 다이렉팅 혹은 데이터베이스 활용(?))/Upper, Front 색 다르게 매칭
            if str(obj.data).find("armond_project_") >= 0:
                # QR 코드 둘레에 사격형 표시

                # Upper, Front, 색상 쌍
                up_fro = {'_upper_': (255, 0, 0), '_front_': (0, 255, 0)}

                for i in range(0, 3):
                    for j in list(up_fro.keys()):
                        if str(obj.data).find(j) >= 0:
                            cv2.line(frame, (obj.polygon[i].x, obj.polygon[i].y), (obj.polygon[i + 1].x,
                                                                                   obj.polygon[i + 1].y), up_fro[j], 3)
                            if i == 0:
                                cv2.line(frame, (obj.polygon[0].x, obj.polygon[0].y), (obj.polygon[3].x,
                                                                                       obj.polygon[3].y), up_fro[j], 3)

        cv2.imshow('Armond_project_alpha', frame)

        # w 키 입력시 종료
        if cv2.waitKey(1) & 0xFF == 27:
            break
else:
    print("can't open CAM_", CAM_NUM, sep='')
    exit()

cap.release()
cv2.destroyAllWindows()
