import cv2
import dlib

hog_face_detector = dlib.get_frontal_face_detector()

img = cv2.imread("demo3face.jpeg")

grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = hog_face_detector(grayImg)

for id,rect in enumerate(faces):
    x1 = rect.left()
    y1 = rect.top()
    x2 = rect.right()
    y2 = rect.bottom()
    cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)

cv2.imshow("Framing", img)
cv2.waitKey(0)
cv2.destroyAllWindows()