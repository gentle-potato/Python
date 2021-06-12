# 입력한 정수가 양수, 음수, 0인 판별하여 출력

number = int(input('정수입력 : '))

if number>0:
    print('양수')
else:
    if number<0 :
        print('음수')
    else:
        print('0')

if number>=0:
    if(number==0):
        print('0')
    else:
        print('양수')
else:
    print('음수')


if(number>0):
    print('양수')
elif(number<0):
    print('음수')
else:
    print('0')