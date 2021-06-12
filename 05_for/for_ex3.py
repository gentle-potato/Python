# 리스트에 저장되어 있는 성적에 따라 합격/불합격을 판별하시오.
# 성적이 60점 이상이면 합격, 아니면 불합격 처리하시오.
# 출력 양식 : 리스트 저장 순서에 따라

print('# 예시')
scores = [90, 57, 88, 45, 78]
num = 0

for score in scores :
    num += 1
    if score >= 60 :
        result = '합격'
    else :
        result = '불합격'
    print('%d번 %d점 %s' % (num, score, result))

# ==============================

print('\n==============================\n')

# 숫자 10개를 입력 받아서 양, 음, 0의 개수 출력
list1 = int(input('숫자1 입력 : ')) ; list2 = int(input('숫자2 입력 : '))
list3 = int(input('숫자3 입력 : ')) ; list4 = int(input('숫자4 입력 : '))
list5 = int(input('숫자5 입력 : ')) ; list6 = int(input('숫자6 입력 : '))
list7 = int(input('숫자7 입력 : ')) ; list8 = int(input('숫자8 입력 : '))
list9 = int(input('숫자9 입력 : ')) ; list10 = int(input('숫자10 입력 : '))

list = [list1, list2, list3, list4, list5, list6, list7, list8, list9, list10]
num = 0
plus = 0 ; minus = 0 ; zero = 0

for n in list :
    num += 1
    if n > 0 :
        plus += 1
    elif n < 0 :
        minus += 1
    else :
        zero += 1

print('------------------')
print(f'양의 개수 : {plus}\n음의 개수 : {minus}\n0의 개수 : {zero}')

print('\n# 또 다른 방법\n')
positive = negative = young = 0

for i in range(1, 11) :
    number = int(input('숫자 %d 입력 : ' % i))
    if number > 0 :
        positive += 1
    elif number < 0 :
        minus += 1
    else :
        young += 1
print('------------------')
print(f'양의 개수 : {positive}\n음의 개수 : {negative}\n0의 개수 : {young}')