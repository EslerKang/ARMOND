import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar


cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

# 너비
cap.set(3, 640)

# 높이
cap.set(4, 480)
if cap.isOpened():
    detector = cv2.QRCodeDetector()
    while True:
        _, frame = cap.read()

        # 흑백영상으로 바꿈
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        decodedObjects = pyzbar.decode(frame)
        for obj in decodedObjects:

            # QR 코드값 화면에 출력
            cv2.putText(frame, str(obj.data), (50, 50), font, 2, (255, 0, 0), 3)

            # QR 코드 둘레에 사격형 표시
            for i in range(0,3):
                cv2.line(frame, (obj.polygon[i].x, obj.polygon[i].y), (obj.polygon[i+1].x, obj.polygon[i+1].y), (255, 0, 0), 3)
            cv2.line(frame, (obj.polygon[0].x, obj.polygon[0].y), (obj.polygon[3].x, obj.polygon[3].y), (255, 0, 0), 3)

        cv2.imshow('frame', frame)
        # w 키 입력시 종료
        if cv2.waitKey(1) & 0xFF == ord('w'):
            break

cap.release()
cv2.destroyAllWindows()
