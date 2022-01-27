import cv2
import mediapipe
import faceTracker as ft

cap = cv2.VideoCapture(1)
tracker = ft.faceDetector(min_detection_confidence = 0.75)

while True:
    ret, frame = cap.read()
    if ret:
        _, img = tracker.findFaces(frame)
        cv2.imshow("Framing", img)
    else:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()