import cv2
import numpy as np


face_classifier = cv2.CascadeClassifier('./templates/haarcascade_frontalface_default.xml')


def face_extractor(img):

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)

    if faces ==():
        return None

    for(x,y,w,h) in faces:
        cropped_face = img[y:y+h, x:x+w]

    return cropped_face


print("Please enter a name to register for a new account.")
new_account_name = input();


print("Start face recognition. Align your face to the front cam.")
cap = cv2.VideoCapture(0)
count = 0

while True:
    ret, frame = cap.read()
    if face_extractor(frame) is not None:
        count += 1
        print("Face Founded!")
        face = cv2.resize(face_extractor(frame),(200,200))
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        file_name_path = './users/' + new_account_name + '.jpg'
        cv2.imwrite(file_name_path,face)

    else:
        print("Face not Found")
        pass

    if cv2.waitKey(1)==13 or count == 1:
        cap.release()
        cv2.destroyAllWindows()
        break


cap.release()
cv2.destroyAllWindows()


print('New account registration is complete.')



