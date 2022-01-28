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

------------------------------------
Project Face Tracking with Mediapipe
------------------------------------

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

<p align = "center">
    <img src = "https://github.com/Raihan-009/openCV_FaceDetection/blob/main/results/faceTracking01.png">
</p>


-----------------------------------
Haar Cascade Classifier
-----------------------------------

<p>Object Detection using Haar feature-based cascade classifiers is an effective object detection method proposed by Paul Viola and Michael Jones in their paper, "Rapid Object Detection using a Boosted Cascade of Simple Features" in 2001. It is a machine learning based approach where a cascade function is trained from a lot of positive and negative images. It is then used to detect objects in other images.</p>

You can get necessary haarcascade file here [harcascade_frontalface_default.xml](https://github.com/Raihan-009/openCV_FaceDetection/blob/main/haar_face.xml)


---------------------------------------------------
Project Face Detection with Haar Cascade Classifier
---------------------------------------------------

> For Static Face Detection 

```python
import cv2
import faceDetector as fd
img = cv2.imread("/Users/Shinigami/Desktop/openCV_FaceDetection/demoface.jpeg")

tracker = fd.faceDetection(scaleFactor=2)

_, img = tracker.findFaces(img)

cv2.imshow("Framing", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

<p align = "center">
    <img src = "https://github.com/Raihan-009/openCV_FaceDetection/blob/main/results/staticFaceDetection.png">
</p>

> For Dynamic or Real Time Face Detection

```python
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
```
