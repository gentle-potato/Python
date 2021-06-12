# 이름 리스트에 해당하는 이름이 있는 경우 이름이 있음을 출력한다.

names = ['홍길동', '이몽룡', '성춘향', '변학도']

inputName = input('이름 입력 : ')

for name in names :
    if inputName == name :
        flag = True
        break   # 반복문 탈출(종료)
    else :
        flag = False

if flag == True :   # True 없이 if flag : 만 입력해도 똑같음
    print('명단에 있습니다.')
else :
    print('명단에 없습니다.')