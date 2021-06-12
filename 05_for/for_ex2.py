# 두 숫자를 입력받아서 이 수 사이의 숫자의 합을 구하기
num1 = int(input('시작 숫자를 입력하시오 : '))
num2 = int(input('시작 숫자를 입력하시오 : '))
total = 0

if num1 <= num2 :
    for i in range(num1, num2 + 1) :
        total += i
else :
    for i in range(num2, num1 + 1) :
        total += i
print('{}과(와) {} 사이의 합은 {}'.format(num1, num2, total))
print(f'{num1}과(와) {num2} 사이의 합은 {total}')   # 형식 알아두기!

print('\n===========================\n')

# 단 수를 입력받아서 해당 구구단 출력
a = int(input('단 수 입력 : '))

for n in range(1, 10) :
    b = a * n
    print('{} * {} = {}'.format(a, n, b))

print('\n===========================\n')

# 카운트 다운 프로그램 작성
x = int(input('시작 숫자를 입력하시오 : '))

for y in range(x, 0, -1) :
    x -= y   # 이 부분 안 적어도 상관 없음!
    print(y, end = ' ')
print('발사')