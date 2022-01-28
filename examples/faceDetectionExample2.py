import cv2
import faceDetector as fd
img = cv2.imread("/Users/Shinigami/Desktop/openCV_FaceDetection/demoface.jpeg")

tracker = fd.faceDetection(scaleFactor=2)

_, img = tracker.findFaces(img)

cv2.imshow("Framing", img)
cv2.waitKey(0)
cv2.destroyAllWindows()