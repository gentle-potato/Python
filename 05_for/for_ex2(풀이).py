#1
num1 = int(input('숫자1 입력 : '))
num2 = int(input('숫자2 입력 : '))
sum = 0

if num1 <= num2 :
    for i in range(num1, num2 + 1) :
        sum += i
else :
    for i in range(num2, num1 + 1) :
        sum += i
print('%d과(와) %d 사이의 합은 %d' % (num1, num2, sum))

#2
dan = int(input('단 수 입력 : '))
for n in range(1, 10) :
    print('%d * %d = %2d' % (dan, n, dan * n))   # %2d로 출력할 때 좀 더 깔끔하게 정렬 가능!

#3
count = int(input('시작 숫자를 입력하시오 : '))
for x in range(count, 0, -1) :
    print('%d' % x, end = ' ')
print('발사')