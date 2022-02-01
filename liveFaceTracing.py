import cv2
import dlib

face_detector = dlib.get_frontal_face_detector()

cap = cv2.VideoCapture("Video.mp4")

while True:
    ret, frame = cap.read()
    if ret:
        faces = face_detector(frame)
        for id,rect in enumerate(faces):
            x1 = rect.left()
            y1 = rect.top()
            x2 = rect.right()
            y2 = rect.bottom()
            cv2.rectangle(frame,(x1,y1), (x2,y2),(0,255,0),2)
        cv2.imshow("Framing",frame)
    else:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()