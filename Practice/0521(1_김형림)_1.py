print('#1 회원 리스트')

customers = []

for i in range(3) :
    customer = str(input('회원 입력 : '))
    customers.append(customer)

print('회원 명단 : ', end ='')
for i in range(3) :
    print(customers[i], end = ' ')
# 또는
# for i in customers :
#     print(i, end = '')

print('\n=============================\n')

print('#2 점수 리스트')

scores = []

students = int(input('학생 수 입력 : '))

score = total = over_80 = 0
for x in range(students) :
    score = int(input(f'학생{x+1} 점수 입력 : '))
    scores.append(score)
    total += score
print(f'총점 : {total}\n평균 : {total/students:.2f}')

for x in range(len(scores)) :
    if scores[x] >= 80 :
        over_80 += 1
    else :
        pass
print(f'80점 이상 학생 : {over_80}명')

print('\n=============================\n')

print('#3 상품 리스트')

goods = []

good = (input('상품 등록 (엔터키 누르면 종료) : '))

while good != '' :
    goods.append(good)
    good = (input('상품 등록 (엔터키 누르면 종료) : '))
# 또는
# if good == '' :
#     break
# else :
#     goods.append(good)

print('등록된 상품 : ', end = '')
for a in range(len(goods)) :
    print(goods[a], end = ' ')