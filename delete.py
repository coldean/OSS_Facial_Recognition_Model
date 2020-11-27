import os
import shutil
while True:
    num = int(input('1. 유저 정보 삭제 2. 등록된 사진 삭제 3. 나가기: '))
    if num == 1:
      user = input('본인의 이름을 알려주세요: ')
      usero = 'users/' + user
      pinnum = int(input("pin 번호를 입력해주세요: "))
      if os.path.isdir(usero):
        pinfile = open(usero + '/pin.txt', "r")
        pin = int(pinfile.readline())
        if pinnum == pin:
          oxo = int(input('정말로 본인의 정보를 모두 삭제하시겠습니까?(복구 불가능) 1. 예 2. 아니오: '))
          if oxo == 1:
            shutil.rmtree(usero)
            print(user, '님의 정보가 모두 삭제 되었습니다.')
          elif oxo == 2:
              print('삭제를 취소 하셨습니다.')
        else:
            print('pin이 일치 하지 않습니다.')
      else:
          print(user, '님의 정보가 존재하지 않습니다.')
    elif num == 2:
        user = input('본인의 이름을 알려주세요: ')
        usert = 'users/'+ user + '/' + user + '.jpg'
        pinnum = int(input("pin 번호를 입력해주세요: "))
        if os.path.isdir('users/'+ user):
          pinfile = open('users/'+ user + '/pin.txt', "r")
          pin = int(pinfile.readline())
          if pinnum == pin:
            if os.path.isfile(usert):
              oxt = int(input('정말로 본인의 사진을 삭제하시겠습니까?(복구 불가능) 1. 예 2. 아니오: '))
              if oxt == 1:
                os.remove(usert)
                print(user, '님의 사진이 삭제 되었습니다.')
              elif oxt == 2:
                  print('삭제를 취소 하셨습니다.')
            else:
                print(user, '님의 사진이 존재하지 않습니다.')
          else:
              print('pin이 일치 하지 않습니다.')
        else:
            print(user, '님의 정보가 존재하지 않습니다.')
    elif num == 3:
        break
    else :
        print('올바른 번호를 입력해주십시오.')
