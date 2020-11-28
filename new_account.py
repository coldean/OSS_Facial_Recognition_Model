import os
import cv2
import numpy as np

def new_account():
    face_classifier = cv2.CascadeClassifier('./templates/haarcascade_frontalface_default.xml')
    
    def face_extractor(img): 
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray,1.3,5)
    
        if faces ==():
            return None
    
        for(x,y,w,h) in faces:
            cropped_face = img[y:y+h, x:x+w]
    
        return cropped_face
        
       
    def createFolder(directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print ('Error: Creating directory. ' +  directory)


    print("Please enter a name to register for a new account.")
    new_account_name = input(); #계정 이름을 사용자에게 입력받음.
    
    createFolder('./users/' + new_account_name)
    
    print("Start face recognition. Align your face to the front cam.")
    cap = cv2.VideoCapture(0) #얼굴 인식 시작
    count = 0
    
    while True: #얼굴이 인식될 때까지 캠 작동
        ret, frame = cap.read() 
        if face_extractor(frame) is not None: #얼굴이 인식되면 인식된 얼굴을 저장 (./users/Kim/Kim.jpg)
            count += 1
            print("Face Founded!")
            face = cv2.resize(face_extractor(frame),(200,200))
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
    
            file_name_path = './users/' + new_account_name + '/' + new_account_name + '.jpg'
            cv2.imwrite(file_name_path,face)
        else: #얼굴이 인식되지 않으면, 인식될 때까지 계속 진행.
            print("Face not Found")
            pass
    
        if cv2.waitKey(1)==13 or count == 1:
            cap.release()
            cv2.destroyAllWindows()
            break
    
    cap.release()
    cv2.destroyAllWindows()
    
    print('New account registration is complete.') #새로운 계정 등록 완료
    
    
