import os
import shutil
def del_face():
    while True:
        num = int(input('1. 유저 정보 삭제 2. 등록된 사진 삭제 3. 나가기: '))
        if num == 1: # 1번 선택
          user = input('본인의 이름을 알려주세요: ')
          usero = 'users/' + user # 폴더 경로 확인
          pinnum = int(input("pin 번호를 입력해주세요: "))
          if os.path.isdir(usero): # 유저의 폴더가 존재
            pinfile = open(usero + '/pin.txt', "r")
            pin = int(pinfile.readline()) # pin.txt 읽음
            if pinnum == pin: # pin이 일치
              oxo = int(input('정말로 본인의 정보를 모두 삭제하시겠습니까?(복구 불가능) 1. 예 2. 아니오: '))
              if oxo == 1: # 1번 선택
                shutil.rmtree(usero) # 폴더 삭제
                print(user, '님의 정보가 모두 삭제 되었습니다.')
              elif oxo == 2: # 2번 선택
                  print('삭제를 취소 하셨습니다.')
            else: # pin이 불일치
                print('pin이 일치 하지 않습니다.')
          else: # 유저의 폴더가 존재하지 않음
              print(user, '님의 정보가 존재하지 않습니다.')
        elif num == 2: # 2번 선택
            user = input('본인의 이름을 알려주세요: ')
            usert = 'users/'+ user + '/' + user + '.jpg' # 사진 경로 확인
            pinnum = int(input("pin 번호를 입력해주세요: "))
            if os.path.isdir('users/'+ user): # 유저의 폴더가 존재
              pinfile = open('users/'+ user + '/pin.txt', "r")
              pin = int(pinfile.readline()) # pin.txt 읽음
              if pinnum == pin: # pin이 일치
                if os.path.isfile(usert): # 유저의 사진이 존재
                  oxt = int(input('정말로 본인의 사진을 삭제하시겠습니까?(복구 불가능) 1. 예 2. 아니오: '))
                  if oxt == 1: # 1번 선택
                    os.remove(usert) # 사진 삭제
                    print(user, '님의 사진이 삭제 되었습니다.')
                  elif oxt == 2: # 2번 선택
                      print('삭제를 취소 하셨습니다.')
                else: # 유저의 사진이 존재 하지 않음
                    print(user, '님의 사진이 존재하지 않습니다.')
              else: # pin이 불일치
                  print('pin이 일치 하지 않습니다.')
            else: # 유저의 폴더가 존재하지 않음
                print(user, '님의 정보가 존재하지 않습니다.')
        elif num == 3: # 3번 선택
            break #종료
        else : # 1, 2, 3번 외의 번호 입력
            print('올바른 번호를 입력해주십시오.')
