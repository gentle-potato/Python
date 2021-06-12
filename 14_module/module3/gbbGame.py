def gbb_game(you_n) :
    from random import randint
    com_n = randint(1, 3)
    if com_n - you_n in (-2, 1) :
        print('컴퓨터가 이겼습니다.')
    elif com_n - you_n == 0 :
        print('비겼습니다.')
    else :
        print('당신이 이겼습니다.')
    if com_n == 1 :
        com_n = '가위'
    elif com_n == 2 :
        com_n = '바위'
    else :
        com_n = '보'
    print('COM : %s' % com_n)
    return com_n, you_n

def input_num() :
    you_n = int(input('YOU 입력 (1:가위, 2:바위, 3:보) : '))
    gbb_game(you_n)
    if you_n == 1 :
        you_n = '가위'
    elif you_n == 2 :
        you_n = '바위'
    else :
        you_n = '보'
    print('YOU : %s' % you_n)