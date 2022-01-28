import cv2

class faceDetection():
    def __init__ (self, scaleFactor=1.1,minNeighbors = 3, flags = 0, minSize = False, maxSize = False):
        self.face_cascade = cv2.CascadeClassifier("/Users/Shinigami/Desktop/openCV_FaceDetection/haar_face.xml")
        self.scaleFactor = scaleFactor
        self.minNeighbors = minNeighbors
        self.minSize = minSize
        self.maxSize = maxSize

    def findFaces(self,img):
        grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        self.faces = self.face_cascade.detectMultiScale(grayImg, self.scaleFactor,self.minNeighbors)
        bbox = []
        if (len(self.faces) != 0):
            for x,y,w,h in self.faces:
                bbox.append([x,y,w,h])
                cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,255), 2)
        return bbox, img
def main():
    cap = cv2.VideoCapture(0)
    tracker = faceDetection()

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

if __name__ == "__main__":
    main()