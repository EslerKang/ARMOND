import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 640)
#WIDTH

cap.set(4, 480)
#HEIGHT

face_cascade = cv2.CascadeClassifier('haarcascade_frontface.xml')

while(True):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    #count faces
    if cv2.waitKey(1) & 0xFF == ord('c'):
        print(len(faces))

    #make rectangular shape on the face
    for (x,y,w,h) in faces:
         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)

    #output
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('w'):
        break

cap.release()
cv2.destroyAllWindows()