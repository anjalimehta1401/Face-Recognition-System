import cv2
import numpy as np


face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


def face_extractor(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    if faces is ():
        return None
    for (x, y, w, h) in faces:
        cropped_faces = img[y:y+h, x:x+w]

    return cropped_faces


cap = cv2.VideoCapture(0)

count = 0

while True:
    ret, frame = cap.read()

    if face_extractor(frame) is not None:
        count += 1
        face = cv2.resize(face_extractor(frame),(300,300))
        #face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)


        file_name ='C:/Users/abhin/Desktop/abhinav/projects/Facial Recognition Based Attendance System/user data/user'+ str(count)+ '.jpg'
        cv2.imwrite(file_name, face)
        cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
        cv2.imshow('face cropper', face)

    else:
        #print("Face not  found")
        pass

    if cv2.waitKey(1) == 27 or count == 50:
        break


cap.release()
cv2.destroyAllWindows()
print(' SAMPlES COlLECTED ')
import login