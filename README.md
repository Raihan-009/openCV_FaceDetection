# openCV_FaceDetection
openCV face detection projects


## Necessarry dependencies
<p> You can simply pip to install necessarry module. </p>

<code>pip install opencv-python</code>

<code>pip install mediapipe</code>

-----------------------------------
Mediapipe
-----------------------------------
<p> MediaPipe Face Detection is an ultrafast face detection solution that comes with 6 landmarks and multi-face support.  </p>

-----------------------------------
Project Face Tracking
-----------------------------------

<p align = "center">
    <img src = "https://github.com/Raihan-009/openCV_FaceDetection/blob/main/results/faceTracking01.png">
</p>


```python
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
```
