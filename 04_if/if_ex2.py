# 입력한 정수가 양수, 음수, 0인 경우

number = int(input('정수 입력 : '))

if(number > 0) :
    print('양수')
else :
    if(number < 0) :
        print('음수')
    else :
        print('0')

# 또는 elif를 사용하여
if number > 0 :
    print('양수')
elif number < 0 :
    print('음수')
else :
    print('0')