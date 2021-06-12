# continue문 : 조건이 참일 경우 반복문 계속 수행
x = 0

while x < 10 :
    x += 1
    if x % 2 == 0 :   # 짝수
        continue

    print(x)

# 무한 반복(Loop)
# break문 : 조건이 참일 경우 반복문 종료
print('반복 시작')

while True :
    answer = input('종료하려면 x 입력 : ')
    if answer == 'x' :
        break

print('반복 종료')