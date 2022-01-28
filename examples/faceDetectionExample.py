import cv2
import faceDetector as fd

cap = cv2.VideoCapture(0)
tracker = fd.faceDetection()
while True:
    ret, frame = cap.read()
    if ret:
        _ , img = tracker.findFaces(frame)
        cv2.imshow("Framing", img)
    else:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()