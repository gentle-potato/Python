# 숫자 10개 입력받아서 양, 음, 0의 개수 구하기

pos, zero, neg = 0, 0, 0

for i in range(10) :
    number = int(input('숫자{} 입력 : '.format(i + 1)))
    # input('숫자%d 입력 : ') % (i + 1))
    if number > 0 :
        pos += 1
    elif number == 0 :
        zero += 1
    else :
        neg += 1

print('------------------')
print('양의 개수 : %d' % pos)
print('음의 개수 : %d' % neg)
print('0의 개수 : %d' % zero)